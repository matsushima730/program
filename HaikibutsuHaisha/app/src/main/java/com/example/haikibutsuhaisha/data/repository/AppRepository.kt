package com.example.haikibutsuhaisha.data.repository

import com.example.haikibutsuhaisha.data.AppDatabase
import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.entity.Truck

class AppRepository(private val db: AppDatabase) {
    private val truckDao = db.truckDao()
    private val driverDao = db.driverDao()
    private val clientDao = db.clientDao()
    private val assignmentDao = db.assignmentDao()

    // Trucks
    fun trucks() = truckDao.observeAll()
    suspend fun upsertTruck(t: Truck) = truckDao.upsert(t)
    suspend fun deleteTruck(t: Truck) = truckDao.delete(t)
    suspend fun getTruck(id: Long) = truckDao.getById(id)

    // Drivers
    fun drivers() = driverDao.observeAll()
    suspend fun upsertDriver(d: Driver) = driverDao.upsert(d)
    suspend fun deleteDriver(d: Driver) = driverDao.delete(d)
    suspend fun getDriver(id: Long) = driverDao.getById(id)

    // Clients
    fun clients() = clientDao.observeAll()
    fun clientsByKind(kind: ClientKind) = clientDao.observeByKind(kind)
    suspend fun upsertClient(c: Client) = clientDao.upsert(c)
    suspend fun deleteClient(c: Client) = clientDao.delete(c)
    suspend fun getClient(id: Long) = clientDao.getById(id)

    // Assignments
    fun assignmentsByDate(date: String) = assignmentDao.observeByDate(date)
    fun assignmentDatesInRange(from: String, to: String) = assignmentDao.observeDatesInRange(from, to)
    suspend fun upsertAssignment(a: Assignment) = assignmentDao.upsert(a)
    suspend fun deleteAssignment(a: Assignment) = assignmentDao.delete(a)
    suspend fun getAssignment(id: Long) = assignmentDao.getById(id)
}
