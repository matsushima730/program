package com.example.haikibutsuhaisha.data.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import com.example.haikibutsuhaisha.data.entity.Truck
import kotlinx.coroutines.flow.Flow

@Dao
interface TruckDao {
    @Query("SELECT * FROM trucks ORDER BY plateNumber")
    fun observeAll(): Flow<List<Truck>>

    @Query("SELECT * FROM trucks WHERE id = :id")
    suspend fun getById(id: Long): Truck?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(truck: Truck): Long

    @Update
    suspend fun update(truck: Truck)

    @Delete
    suspend fun delete(truck: Truck)
}
