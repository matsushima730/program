package com.example.haikibutsuhaisha.ui.common

import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.haikibutsuhaisha.HaikibutsuApp
import com.example.haikibutsuhaisha.data.repository.AppRepository

@Composable
fun rememberRepository(): AppRepository {
    val ctx = LocalContext.current.applicationContext as HaikibutsuApp
    return ctx.repository
}

@Composable
inline fun <reified VM : ViewModel> viewModelWithRepo(
    crossinline build: (AppRepository) -> VM
): VM {
    val repo = rememberRepository()
    val factory = object : ViewModelProvider.Factory {
        @Suppress("UNCHECKED_CAST")
        override fun <T : ViewModel> create(modelClass: Class<T>): T = build(repo) as T
    }
    return viewModel(factory = factory)
}
