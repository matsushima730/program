package com.example.haikibutsuhaisha

import android.app.Application
import com.example.haikibutsuhaisha.data.AppDatabase
import com.example.haikibutsuhaisha.data.SeedData
import com.example.haikibutsuhaisha.data.repository.AppRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch

class HaikibutsuApp : Application() {
    lateinit var repository: AppRepository
        private set

    private val appScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    override fun onCreate() {
        super.onCreate()
        val db = AppDatabase.get(this)
        repository = AppRepository(db)
        appScope.launch { SeedData.seedIfEmpty(db) }
    }
}
