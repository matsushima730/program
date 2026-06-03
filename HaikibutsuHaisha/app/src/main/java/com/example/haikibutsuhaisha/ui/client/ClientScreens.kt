package com.example.haikibutsuhaisha.ui.client

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
import androidx.compose.material3.AssistChip
import androidx.compose.material3.AssistChipDefaults
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
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import com.example.haikibutsuhaisha.data.repository.AppRepository
import com.example.haikibutsuhaisha.ui.common.DropdownField
import com.example.haikibutsuhaisha.ui.common.viewModelWithRepo
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

private class ClientListViewModel(repo: AppRepository) : ViewModel() {
    val clients: StateFlow<List<Client>> = repo.clients()
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ClientListScreen(onEdit: (Long) -> Unit) {
    val vm = viewModelWithRepo { ClientListViewModel(it) }
    val list by vm.clients.collectAsStateWithLifecycle()

    Scaffold(
        topBar = { TopAppBar(title = { Text("取引先一覧") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = { onEdit(0L) }) {
                Icon(Icons.Default.Add, contentDescription = "取引先を追加")
            }
        }
    ) { padding ->
        if (list.isEmpty()) {
            Column(Modifier.fillMaxSize().padding(padding),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally) {
                Text("取引先が登録されていません", color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
            return@Scaffold
        }
        LazyColumn(
            modifier = Modifier.fillMaxSize().padding(padding),
            contentPadding = PaddingValues(12.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(list, key = { it.id }) { c ->
                Card(Modifier.fillMaxWidth().clickable { onEdit(c.id) }) {
                    Column(Modifier.padding(12.dp)) {
                        androidx.compose.foundation.layout.Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(c.name, style = MaterialTheme.typography.titleMedium,
                                modifier = Modifier.weight(1f))
                            AssistChip(
                                onClick = {},
                                enabled = false,
                                label = { Text(c.kind.label) },
                                colors = AssistChipDefaults.assistChipColors(
                                    disabledContainerColor = when (c.kind) {
                                        ClientKind.GENERATOR -> MaterialTheme.colorScheme.secondaryContainer
                                        ClientKind.DISPOSAL -> MaterialTheme.colorScheme.tertiaryContainer
                                    },
                                    disabledLabelColor = MaterialTheme.colorScheme.onSurface
                                )
                            )
                        }
                        if (c.address.isNotBlank())
                            Text(c.address, style = MaterialTheme.typography.bodyMedium,
                                color = MaterialTheme.colorScheme.onSurfaceVariant)
                        if (c.contactPerson.isNotBlank() || c.phone.isNotBlank())
                            Text("${c.contactPerson}  ${c.phone}",
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant)
                    }
                }
            }
        }
    }
}

private class ClientEditViewModel(private val repo: AppRepository) : ViewModel() {
    val draft = MutableStateFlow(Client(name = ""))
    val isNew = MutableStateFlow(true)

    fun load(id: Long) {
        viewModelScope.launch {
            if (id == 0L) {
                draft.value = Client(name = ""); isNew.value = true
            } else {
                draft.value = repo.getClient(id) ?: draft.value
                isNew.value = false
            }
        }
    }
    fun save(onDone: () -> Unit) = viewModelScope.launch { repo.upsertClient(draft.value); onDone() }
    fun delete(onDone: () -> Unit) = viewModelScope.launch {
        if (draft.value.id != 0L) repo.deleteClient(draft.value); onDone()
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ClientEditScreen(id: Long, onDone: () -> Unit) {
    val vm = viewModelWithRepo { ClientEditViewModel(it) }
    LaunchedEffect(id) { vm.load(id) }
    val c by vm.draft.collectAsStateWithLifecycle()
    val isNew by vm.isNew.collectAsStateWithLifecycle()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(if (isNew) "取引先を追加" else "取引先を編集") },
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
                value = c.name,
                onValueChange = { v -> vm.draft.value = c.copy(name = v) },
                label = { Text("取引先名") },
                modifier = Modifier.fillMaxWidth()
            )
            DropdownField(
                label = "区分",
                items = ClientKind.entries,
                selected = c.kind,
                itemLabel = { it.label },
                onSelect = { sel -> vm.draft.value = c.copy(kind = sel ?: ClientKind.GENERATOR) },
                allowClear = false
            )
            OutlinedTextField(
                value = c.address,
                onValueChange = { v -> vm.draft.value = c.copy(address = v) },
                label = { Text("住所") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = c.contactPerson,
                onValueChange = { v -> vm.draft.value = c.copy(contactPerson = v) },
                label = { Text("担当者") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = c.phone,
                onValueChange = { v -> vm.draft.value = c.copy(phone = v) },
                label = { Text("電話") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = c.notes,
                onValueChange = { v -> vm.draft.value = c.copy(notes = v) },
                label = { Text("備考") },
                minLines = 2,
                modifier = Modifier.fillMaxWidth()
            )
            Button(
                onClick = { vm.save(onDone) },
                enabled = c.name.isNotBlank(),
                modifier = Modifier.fillMaxWidth()
            ) { Text(if (isNew) "登録" else "更新") }
        }
    }
}
