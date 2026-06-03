package com.example.haikibutsuhaisha.ui.truck

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.haikibutsuhaisha.data.entity.BodyType
import com.example.haikibutsuhaisha.data.entity.Truck
import com.example.haikibutsuhaisha.data.repository.AppRepository
import com.example.haikibutsuhaisha.ui.common.DropdownField
import com.example.haikibutsuhaisha.ui.common.viewModelWithRepo
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

private class TruckListViewModel(repo: AppRepository) : ViewModel() {
    val trucks: StateFlow<List<Truck>> = repo.trucks()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TruckListScreen(onEdit: (Long) -> Unit) {
    val vm = viewModelWithRepo { TruckListViewModel(it) }
    val list by vm.trucks.collectAsStateWithLifecycle()

    Scaffold(
        topBar = { TopAppBar(title = { Text("車両一覧") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = { onEdit(0L) }) {
                Icon(Icons.Default.Add, contentDescription = "車両を追加")
            }
        }
    ) { padding ->
        if (list.isEmpty()) {
            Column(Modifier.fillMaxSize().padding(padding),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = androidx.compose.ui.Alignment.CenterHorizontally) {
                Text("車両が登録されていません", color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
            return@Scaffold
        }
        LazyColumn(
            modifier = Modifier.fillMaxSize().padding(padding),
            contentPadding = PaddingValues(12.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(list, key = { it.id }) { t ->
                Card(Modifier.fillMaxWidth().clickable { onEdit(t.id) }) {
                    Column(Modifier.padding(12.dp)) {
                        Text(t.plateNumber, style = MaterialTheme.typography.titleMedium)
                        Text("${t.vehicleType} / ${t.bodyType.label} / 積載 ${t.loadCapacityKg} kg",
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant)
                        if (t.makerModel.isNotBlank()) {
                            Text(t.makerModel, style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    }
                }
            }
        }
    }
}

private class TruckEditViewModel(private val repo: AppRepository) : ViewModel() {
    val draft = MutableStateFlow(Truck(plateNumber = "", vehicleType = "", loadCapacityKg = 0))
    val isNew = MutableStateFlow(true)

    fun load(id: Long) {
        viewModelScope.launch {
            if (id == 0L) {
                draft.value = Truck(plateNumber = "", vehicleType = "", loadCapacityKg = 0)
                isNew.value = true
            } else {
                draft.value = repo.getTruck(id) ?: draft.value
                isNew.value = false
            }
        }
    }

    fun save(onDone: () -> Unit) = viewModelScope.launch {
        repo.upsertTruck(draft.value); onDone()
    }
    fun delete(onDone: () -> Unit) = viewModelScope.launch {
        if (draft.value.id != 0L) repo.deleteTruck(draft.value); onDone()
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TruckEditScreen(id: Long, onDone: () -> Unit) {
    val vm = viewModelWithRepo { TruckEditViewModel(it) }
    LaunchedEffect(id) { vm.load(id) }
    val t by vm.draft.collectAsStateWithLifecycle()
    val isNew by vm.isNew.collectAsStateWithLifecycle()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(if (isNew) "車両を追加" else "車両を編集") },
                navigationIcon = {
                    IconButton(onClick = onDone) { Icon(Icons.Default.ArrowBack, contentDescription = "戻る") }
                },
                actions = {
                    if (!isNew) IconButton(onClick = { vm.delete(onDone) }) {
                        Icon(Icons.Default.Delete, contentDescription = "削除")
                    }
                }
            )
        }
    ) { padding ->
        Column(
            Modifier.fillMaxSize().padding(padding).padding(16.dp).verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            OutlinedTextField(
                value = t.plateNumber,
                onValueChange = { v -> vm.draft.value = t.copy(plateNumber = v) },
                label = { Text("プレートナンバー") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = t.vehicleType,
                onValueChange = { v -> vm.draft.value = t.copy(vehicleType = v) },
                label = { Text("車種 (例: 4t, 10t)") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = if (t.loadCapacityKg == 0) "" else t.loadCapacityKg.toString(),
                onValueChange = { v ->
                    val n = v.filter { it.isDigit() }.take(7).toIntOrNull() ?: 0
                    vm.draft.value = t.copy(loadCapacityKg = n)
                },
                label = { Text("最大積載量 (kg)") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                modifier = Modifier.fillMaxWidth()
            )
            DropdownField(
                label = "車両様式",
                items = BodyType.entries,
                selected = t.bodyType,
                itemLabel = { it.label },
                onSelect = { sel -> vm.draft.value = t.copy(bodyType = sel ?: BodyType.OTHER) },
                allowClear = false
            )
            OutlinedTextField(
                value = t.makerModel,
                onValueChange = { v -> vm.draft.value = t.copy(makerModel = v) },
                label = { Text("メーカー・車名") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = t.notes,
                onValueChange = { v -> vm.draft.value = t.copy(notes = v) },
                label = { Text("備考") },
                minLines = 2,
                modifier = Modifier.fillMaxWidth()
            )
            Button(
                onClick = { vm.save(onDone) },
                enabled = t.plateNumber.isNotBlank(),
                modifier = Modifier.fillMaxWidth()
            ) { Text(if (isNew) "登録" else "更新") }
        }
    }
}
