package com.example.haikibutsuhaisha.ui.calendar

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import com.example.haikibutsuhaisha.data.entity.ContainerStatus
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.entity.Truck
import com.example.haikibutsuhaisha.data.repository.AppRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

data class AssignmentEditState(
    val loaded: Boolean = false,
    val isNew: Boolean = true,
    val draft: Assignment = Assignment(
        date = "", truckId = null, driverId = null,
        generatorClientId = null, disposalClientId = null
    ),
    val trucks: List<Truck> = emptyList(),
    val drivers: List<Driver> = emptyList(),
    val generators: List<Client> = emptyList(),
    val disposals: List<Client> = emptyList()
)

class AssignmentEditViewModel(private val repo: AppRepository) : ViewModel() {
    private val draftFlow = MutableStateFlow<Assignment?>(null)
    private val isNewFlow = MutableStateFlow(true)

    val state: StateFlow<AssignmentEditState> = combine(
        draftFlow,
        isNewFlow,
        repo.trucks(),
        repo.drivers(),
        repo.clients()
    ) { draft, isNew, trucks, drivers, clients ->
        AssignmentEditState(
            loaded = draft != null,
            isNew = isNew,
            draft = draft ?: AssignmentEditState().draft,
            trucks = trucks,
            drivers = drivers,
            generators = clients.filter { it.kind == ClientKind.GENERATOR },
            disposals = clients.filter { it.kind == ClientKind.DISPOSAL }
        )
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), AssignmentEditState())

    fun load(date: String, id: Long) {
        viewModelScope.launch {
            if (id == 0L) {
                isNewFlow.value = true
                draftFlow.value = Assignment(
                    date = date,
                    truckId = null, driverId = null,
                    generatorClientId = null, disposalClientId = null
                )
            } else {
                val a = repo.getAssignment(id) ?: Assignment(
                    date = date, truckId = null, driverId = null,
                    generatorClientId = null, disposalClientId = null
                )
                isNewFlow.value = (a.id == 0L)
                draftFlow.value = a
            }
        }
    }

    fun update(transform: (Assignment) -> Assignment) {
        draftFlow.value = draftFlow.value?.let(transform)
    }

    fun save(onDone: () -> Unit) {
        val current = draftFlow.value ?: return
        viewModelScope.launch {
            repo.upsertAssignment(current)
            onDone()
        }
    }

    fun delete(onDone: () -> Unit) {
        val current = draftFlow.value ?: return
        if (current.id == 0L) { onDone(); return }
        viewModelScope.launch {
            repo.deleteAssignment(current)
            onDone()
        }
    }
}
