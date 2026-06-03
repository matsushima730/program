package com.example.haikibutsuhaisha.ui.driver

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
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.repository.AppRepository
import com.example.haikibutsuhaisha.ui.common.viewModelWithRepo
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

private class DriverListViewModel(repo: AppRepository) : ViewModel() {
    val drivers: StateFlow<List<Driver>> = repo.drivers()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DriverListScreen(onEdit: (Long) -> Unit) {
    val vm = viewModelWithRepo { DriverListViewModel(it) }
    val list by vm.drivers.collectAsStateWithLifecycle()

    Scaffold(
        topBar = { TopAppBar(title = { Text("ドライバー一覧") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = { onEdit(0L) }) {
                Icon(Icons.Default.Add, contentDescription = "ドライバーを追加")
            }
        }
    ) { padding ->
        if (list.isEmpty()) {
            Column(Modifier.fillMaxSize().padding(padding),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = androidx.compose.ui.Alignment.CenterHorizontally) {
                Text("ドライバーが登録されていません", color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
            return@Scaffold
        }
        LazyColumn(
            modifier = Modifier.fillMaxSize().padding(padding),
            contentPadding = PaddingValues(12.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(list, key = { it.id }) { d ->
                Card(Modifier.fillMaxWidth().clickable { onEdit(d.id) }) {
                    Column(Modifier.padding(12.dp)) {
                        Text(d.name, style = MaterialTheme.typography.titleMedium)
                        if (d.licenseClass.isNotBlank() || d.phone.isNotBlank()) {
                            Text("${d.licenseClass.ifBlank { "—" }}  ${d.phone}",
                                style = MaterialTheme.typography.bodyMedium,
                                color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    }
                }
            }
        }
    }
}

private class DriverEditViewModel(private val repo: AppRepository) : ViewModel() {
    val draft = MutableStateFlow(Driver(name = ""))
    val isNew = MutableStateFlow(true)

    fun load(id: Long) {
        viewModelScope.launch {
            if (id == 0L) {
                draft.value = Driver(name = ""); isNew.value = true
            } else {
                draft.value = repo.getDriver(id) ?: draft.value
                isNew.value = false
            }
        }
    }
    fun save(onDone: () -> Unit) = viewModelScope.launch { repo.upsertDriver(draft.value); onDone() }
    fun delete(onDone: () -> Unit) = viewModelScope.launch {
        if (draft.value.id != 0L) repo.deleteDriver(draft.value); onDone()
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DriverEditScreen(id: Long, onDone: () -> Unit) {
    val vm = viewModelWithRepo { DriverEditViewModel(it) }
    LaunchedEffect(id) { vm.load(id) }
    val d by vm.draft.collectAsStateWithLifecycle()
    val isNew by vm.isNew.collectAsStateWithLifecycle()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(if (isNew) "ドライバーを追加" else "ドライバーを編集") },
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
                value = d.name,
                onValueChange = { v -> vm.draft.value = d.copy(name = v) },
                label = { Text("氏名") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = d.licenseClass,
                onValueChange = { v -> vm.draft.value = d.copy(licenseClass = v) },
                label = { Text("免許区分 (例: 大型, 中型)") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = d.phone,
                onValueChange = { v -> vm.draft.value = d.copy(phone = v) },
                label = { Text("電話") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = d.notes,
                onValueChange = { v -> vm.draft.value = d.copy(notes = v) },
                label = { Text("備考") },
                minLines = 2,
                modifier = Modifier.fillMaxWidth()
            )
            Button(
                onClick = { vm.save(onDone) },
                enabled = d.name.isNotBlank(),
                modifier = Modifier.fillMaxWidth()
            ) { Text(if (isNew) "登録" else "更新") }
        }
    }
}
