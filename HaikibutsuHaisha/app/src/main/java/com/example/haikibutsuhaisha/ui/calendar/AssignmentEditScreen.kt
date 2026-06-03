package com.example.haikibutsuhaisha.ui.calendar

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.Button
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.haikibutsuhaisha.data.entity.ContainerStatus
import com.example.haikibutsuhaisha.ui.common.DropdownField
import com.example.haikibutsuhaisha.ui.common.TimePickerField
import com.example.haikibutsuhaisha.ui.common.viewModelWithRepo
import com.example.haikibutsuhaisha.util.DateFmt

@OptIn(ExperimentalMaterial3Api::class, ExperimentalLayoutApi::class)
@Composable
fun AssignmentEditScreen(
    date: String,
    assignmentId: Long,
    onDone: () -> Unit
) {
    val vm = viewModelWithRepo { AssignmentEditViewModel(it) }
    LaunchedEffect(date, assignmentId) { vm.load(date, assignmentId) }
    val state by vm.state.collectAsStateWithLifecycle()

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    val parsed = remember(date) { DateFmt.parseDateOrToday(date) }
                    Text(if (state.isNew) "新規配車 — ${parsed.format(DateFmt.JP_DATE)}"
                         else "配車編集 — ${parsed.format(DateFmt.JP_DATE)}")
                },
                navigationIcon = {
                    IconButton(onClick = onDone) { Icon(Icons.Default.ArrowBack, contentDescription = "戻る") }
                },
                actions = {
                    if (!state.isNew) {
                        IconButton(onClick = { vm.delete(onDone) }) {
                            Icon(Icons.Default.Delete, contentDescription = "削除")
                        }
                    }
                }
            )
        }
    ) { padding ->
        if (!state.loaded) return@Scaffold

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(16.dp)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            DropdownField(
                label = "車両",
                items = state.trucks,
                selected = state.trucks.firstOrNull { it.id == state.draft.truckId },
                itemLabel = { "${it.plateNumber} / ${it.vehicleType} (${it.bodyType.label})" },
                onSelect = { sel -> vm.update { it.copy(truckId = sel?.id) } }
            )
            DropdownField(
                label = "ドライバー",
                items = state.drivers,
                selected = state.drivers.firstOrNull { it.id == state.draft.driverId },
                itemLabel = { "${it.name} (${it.licenseClass.ifBlank { "—" }})" },
                onSelect = { sel -> vm.update { it.copy(driverId = sel?.id) } }
            )
            DropdownField(
                label = "排出元 (取引先)",
                items = state.generators,
                selected = state.generators.firstOrNull { it.id == state.draft.generatorClientId },
                itemLabel = { it.name },
                onSelect = { sel -> vm.update { it.copy(generatorClientId = sel?.id) } }
            )
            DropdownField(
                label = "行き先 (処分場/中間処理)",
                items = state.disposals,
                selected = state.disposals.firstOrNull { it.id == state.draft.disposalClientId },
                itemLabel = { it.name },
                onSelect = { sel -> vm.update { it.copy(disposalClientId = sel?.id) } }
            )

            OutlinedTextField(
                value = state.draft.wasteType,
                onValueChange = { v -> vm.update { it.copy(wasteType = v) } },
                label = { Text("廃棄物種類") },
                modifier = Modifier.fillMaxWidth()
            )

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                TimePickerField(
                    label = "発車予定",
                    value = state.draft.departureTime,
                    onValueChange = { v -> vm.update { it.copy(departureTime = v) } },
                    modifier = Modifier.weight(1f)
                )
                TimePickerField(
                    label = "帰着予定",
                    value = state.draft.returnTime,
                    onValueChange = { v -> vm.update { it.copy(returnTime = v) } },
                    modifier = Modifier.weight(1f)
                )
            }

            Text("車両の状態", style = androidx.compose.material3.MaterialTheme.typography.titleSmall)
            FlowRow(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                verticalArrangement = Arrangement.spacedBy(4.dp)
            ) {
                ContainerStatus.entries.forEach { st ->
                    FilterChip(
                        selected = state.draft.containerStatus == st,
                        onClick = { vm.update { it.copy(containerStatus = st) } },
                        label = { Text(st.label) }
                    )
                }
            }

            OutlinedTextField(
                value = state.draft.notes,
                onValueChange = { v -> vm.update { it.copy(notes = v) } },
                label = { Text("備考") },
                minLines = 2,
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(Modifier.width(0.dp))
            Button(
                onClick = { vm.save(onDone) },
                modifier = Modifier.fillMaxWidth()
            ) { Text(if (state.isNew) "登録" else "更新") }
        }
    }
}
