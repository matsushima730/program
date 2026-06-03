package com.example.haikibutsuhaisha.data.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import com.example.haikibutsuhaisha.data.entity.Driver
import kotlinx.coroutines.flow.Flow

@Dao
interface DriverDao {
    @Query("SELECT * FROM drivers ORDER BY name")
    fun observeAll(): Flow<List<Driver>>

    @Query("SELECT * FROM drivers WHERE id = :id")
    suspend fun getById(id: Long): Driver?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(driver: Driver): Long

    @Update
    suspend fun update(driver: Driver)

    @Delete
    suspend fun delete(driver: Driver)
}
