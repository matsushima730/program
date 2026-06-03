package com.example.haikibutsuhaisha.data.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import kotlinx.coroutines.flow.Flow

@Dao
interface ClientDao {
    @Query("SELECT * FROM clients ORDER BY name")
    fun observeAll(): Flow<List<Client>>

    @Query("SELECT * FROM clients WHERE kind = :kind ORDER BY name")
    fun observeByKind(kind: ClientKind): Flow<List<Client>>

    @Query("SELECT * FROM clients WHERE id = :id")
    suspend fun getById(id: Long): Client?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(client: Client): Long

    @Update
    suspend fun update(client: Client)

    @Delete
    suspend fun delete(client: Client)
}
