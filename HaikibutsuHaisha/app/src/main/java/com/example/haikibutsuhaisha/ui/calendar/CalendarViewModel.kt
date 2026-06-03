package com.example.haikibutsuhaisha.ui.calendar

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.entity.Truck
import com.example.haikibutsuhaisha.data.repository.AppRepository
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.flatMapLatest
import kotlinx.coroutines.flow.stateIn
import java.time.LocalDate

data class CalendarUiState(
    val selectedDate: LocalDate = LocalDate.now(),
    val visibleMonth: LocalDate = LocalDate.now().withDayOfMonth(1),
    val daysWithAssignments: Set<LocalDate> = emptySet(),
    val assignments: List<Assignment> = emptyList(),
    val truckById: Map<Long, Truck> = emptyMap(),
    val driverById: Map<Long, Driver> = emptyMap(),
    val clientById: Map<Long, Client> = emptyMap()
)

@OptIn(ExperimentalCoroutinesApi::class)
class CalendarViewModel(private val repo: AppRepository) : ViewModel() {

    private val selectedDate = MutableStateFlow(LocalDate.now())
    private val visibleMonth = MutableStateFlow(LocalDate.now().withDayOfMonth(1))

    private val assignmentsFlow = selectedDate.flatMapLatest { repo.assignmentsByDate(it.toString()) }
    private val datesFlow = visibleMonth.flatMapLatest { m ->
        val from = m.withDayOfMonth(1).toString()
        val to = m.withDayOfMonth(m.lengthOfMonth()).toString()
        repo.assignmentDatesInRange(from, to)
    }

    val state: StateFlow<CalendarUiState> = combine(
        selectedDate,
        visibleMonth,
        assignmentsFlow,
        datesFlow,
        combine(repo.trucks(), repo.drivers(), repo.clients()) { t, d, c ->
            Triple(t.associateBy { it.id }, d.associateBy { it.id }, c.associateBy { it.id })
        }
    ) { sel, month, assigns, dates, maps ->
        CalendarUiState(
            selectedDate = sel,
            visibleMonth = month,
            daysWithAssignments = dates.mapNotNull { runCatching { LocalDate.parse(it) }.getOrNull() }.toSet(),
            assignments = assigns,
            truckById = maps.first,
            driverById = maps.second,
            clientById = maps.third
        )
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), CalendarUiState())

    fun selectDate(d: LocalDate) {
        selectedDate.value = d
        if (d.month != visibleMonth.value.month || d.year != visibleMonth.value.year) {
            visibleMonth.value = d.withDayOfMonth(1)
        }
    }
    fun showMonth(m: LocalDate) { visibleMonth.value = m.withDayOfMonth(1) }
}
