package com.example.haikibutsuhaisha.ui.calendar

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.ChevronLeft
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material3.AssistChip
import androidx.compose.material3.AssistChipDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.ContainerStatus
import com.example.haikibutsuhaisha.ui.common.viewModelWithRepo
import com.example.haikibutsuhaisha.util.DateFmt
import java.time.DayOfWeek
import java.time.LocalDate

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CalendarScreen(
    onEditAssignment: (date: String, id: Long) -> Unit
) {
    val vm = viewModelWithRepo { CalendarViewModel(it) }
    val state by vm.state.collectAsStateWithLifecycle()

    Scaffold(
        topBar = { TopAppBar(title = { Text("配車カレンダー") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = {
                onEditAssignment(state.selectedDate.toString(), 0L)
            }) { Icon(Icons.Default.Add, contentDescription = "配車を追加") }
        }
    ) { padding ->
        Column(Modifier.fillMaxSize().padding(padding)) {
            MonthHeader(
                month = state.visibleMonth,
                onPrev = { vm.showMonth(state.visibleMonth.minusMonths(1)) },
                onNext = { vm.showMonth(state.visibleMonth.plusMonths(1)) }
            )
            MonthGrid(
                month = state.visibleMonth,
                selected = state.selectedDate,
                marked = state.daysWithAssignments,
                onSelect = { vm.selectDate(it) }
            )
            HorizontalDivider()
            Row(
                modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = state.selectedDate.format(DateFmt.JP_DATE),
                    style = MaterialTheme.typography.titleMedium
                )
                Spacer(Modifier.weight(1f))
                Text("${state.assignments.size} 件", color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
            AssignmentList(state, onEditAssignment)
        }
    }
}

@Composable
private fun MonthHeader(month: LocalDate, onPrev: () -> Unit, onNext: () -> Unit) {
    Row(
        modifier = Modifier.fillMaxWidth().padding(horizontal = 8.dp, vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        IconButton(onClick = onPrev) { Icon(Icons.Default.ChevronLeft, contentDescription = "前の月") }
        Text(
            text = month.format(DateFmt.JP_MONTH),
            style = MaterialTheme.typography.titleLarge,
            modifier = Modifier.weight(1f),
            textAlign = androidx.compose.ui.text.style.TextAlign.Center
        )
        IconButton(onClick = onNext) { Icon(Icons.Default.ChevronRight, contentDescription = "次の月") }
    }
}

@Composable
private fun MonthGrid(
    month: LocalDate,
    selected: LocalDate,
    marked: Set<LocalDate>,
    onSelect: (LocalDate) -> Unit
) {
    val first = month.withDayOfMonth(1)
    // 月曜=1...日曜=7。日曜始まりにする為に補正
    val leading = (first.dayOfWeek.value % 7) // Sun=0
    val daysInMonth = month.lengthOfMonth()
    val cells = leading + daysInMonth
    val rows = (cells + 6) / 7

    Column(Modifier.fillMaxWidth().padding(horizontal = 8.dp)) {
        Row(Modifier.fillMaxWidth()) {
            listOf("日", "月", "火", "水", "木", "金", "土").forEachIndexed { i, name ->
                Box(Modifier.weight(1f).padding(vertical = 4.dp), contentAlignment = Alignment.Center) {
                    Text(
                        name,
                        color = when (i) {
                            0 -> Color(0xFFD32F2F); 6 -> Color(0xFF1976D2)
                            else -> MaterialTheme.colorScheme.onSurfaceVariant
                        },
                        fontWeight = FontWeight.SemiBold
                    )
                }
            }
        }
        for (r in 0 until rows) {
            Row(Modifier.fillMaxWidth()) {
                for (c in 0..6) {
                    val cellIndex = r * 7 + c
                    val dayNum = cellIndex - leading + 1
                    if (dayNum in 1..daysInMonth) {
                        val date = first.withDayOfMonth(dayNum)
                        DayCell(
                            date = date,
                            isSelected = date == selected,
                            isMarked = date in marked,
                            onClick = { onSelect(date) },
                            modifier = Modifier.weight(1f)
                        )
                    } else {
                        Box(Modifier.weight(1f).height(44.dp))
                    }
                }
            }
        }
    }
}

@Composable
private fun DayCell(
    date: LocalDate,
    isSelected: Boolean,
    isMarked: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    val isToday = date == LocalDate.now()
    val bg = if (isSelected) MaterialTheme.colorScheme.primary else Color.Transparent
    val fg = when {
        isSelected -> MaterialTheme.colorScheme.onPrimary
        date.dayOfWeek == DayOfWeek.SUNDAY -> Color(0xFFD32F2F)
        date.dayOfWeek == DayOfWeek.SATURDAY -> Color(0xFF1976D2)
        else -> MaterialTheme.colorScheme.onSurface
    }
    Box(
        modifier = modifier
            .padding(2.dp)
            .height(44.dp)
            .clip(RoundedCornerShape(8.dp))
            .clickable(onClick = onClick)
            .then(
                if (isToday && !isSelected)
                    Modifier.border(1.dp, MaterialTheme.colorScheme.primary, RoundedCornerShape(8.dp))
                else Modifier
            )
            .background(bg),
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text("${date.dayOfMonth}", color = fg, fontSize = 14.sp)
            if (isMarked) {
                Box(
                    Modifier
                        .padding(top = 2.dp)
                        .size(6.dp)
                        .clip(CircleShape)
                        .background(if (isSelected) MaterialTheme.colorScheme.onPrimary else MaterialTheme.colorScheme.tertiary)
                )
            }
        }
    }
}

@Composable
private fun AssignmentList(state: CalendarUiState, onEdit: (String, Long) -> Unit) {
    if (state.assignments.isEmpty()) {
        Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            Text("この日の配車はまだありません", color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
        return
    }
    LazyColumn(
        contentPadding = PaddingValues(horizontal = 12.dp, vertical = 8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(state.assignments, key = { it.id }) { a ->
            AssignmentCard(
                a = a,
                truckLabel = state.truckById[a.truckId]?.let { "${it.plateNumber} (${it.vehicleType})" } ?: "車両未割当",
                driverLabel = state.driverById[a.driverId]?.name ?: "ドライバー未割当",
                generatorLabel = state.clientById[a.generatorClientId]?.name ?: "排出元未設定",
                disposalLabel = state.clientById[a.disposalClientId]?.name ?: "処分先未設定",
                onClick = { onEdit(state.selectedDate.toString(), a.id) }
            )
        }
    }
}

@Composable
private fun AssignmentCard(
    a: Assignment,
    truckLabel: String,
    driverLabel: String,
    generatorLabel: String,
    disposalLabel: String,
    onClick: () -> Unit
) {
    Card(
        modifier = Modifier.fillMaxWidth().clickable(onClick = onClick),
        elevation = CardDefaults.cardElevation(defaultElevation = 1.dp)
    ) {
        Column(Modifier.padding(12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Surface(
                    color = MaterialTheme.colorScheme.primary,
                    shape = RoundedCornerShape(6.dp)
                ) {
                    Text(
                        text = (a.departureTime.ifBlank { "--:--" }) + " ▶ " + (a.returnTime.ifBlank { "--:--" }),
                        color = MaterialTheme.colorScheme.onPrimary,
                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp),
                        style = MaterialTheme.typography.labelMedium
                    )
                }
                Spacer(Modifier.width(8.dp))
                StatusChip(a.containerStatus)
            }
            Spacer(Modifier.height(8.dp))
            Text("車両: $truckLabel", style = MaterialTheme.typography.bodyMedium)
            Text("ドライバー: $driverLabel", style = MaterialTheme.typography.bodyMedium)
            Text("排出元: $generatorLabel", style = MaterialTheme.typography.bodyMedium)
            Text("行き先: $disposalLabel", style = MaterialTheme.typography.bodyMedium)
            if (a.wasteType.isNotBlank()) {
                Text("廃棄物: ${a.wasteType}", style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
            if (a.notes.isNotBlank()) {
                Text("備考: ${a.notes}", style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        }
    }
}

@Composable
fun StatusChip(status: ContainerStatus) {
    val color = when (status) {
        ContainerStatus.EMPTY -> MaterialTheme.colorScheme.secondaryContainer
        ContainerStatus.LOADING -> MaterialTheme.colorScheme.tertiaryContainer
        ContainerStatus.LOADED -> MaterialTheme.colorScheme.errorContainer
        ContainerStatus.UNLOADING -> MaterialTheme.colorScheme.tertiaryContainer
        ContainerStatus.RETURNED -> MaterialTheme.colorScheme.surfaceVariant
    }
    AssistChip(
        onClick = {},
        enabled = false,
        label = { Text(status.label) },
        colors = AssistChipDefaults.assistChipColors(
            containerColor = color,
            disabledContainerColor = color,
            disabledLabelColor = MaterialTheme.colorScheme.onSurface
        )
    )
}
