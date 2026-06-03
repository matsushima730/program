package com.example.haikibutsuhaisha.data.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import com.example.haikibutsuhaisha.data.entity.Assignment
import kotlinx.coroutines.flow.Flow

/**
 * 日次配車の表示は JOIN しない素朴な実装でも十分速い (件数が少ない為)。
 * 画面側で各マスタを Map にして突き合わせる。
 */
@Dao
interface AssignmentDao {
    @Query("SELECT * FROM assignments WHERE date = :date ORDER BY departureTime, id")
    fun observeByDate(date: String): Flow<List<Assignment>>

    @Query("SELECT DISTINCT date FROM assignments WHERE date BETWEEN :from AND :to")
    fun observeDatesInRange(from: String, to: String): Flow<List<String>>

    @Query("SELECT * FROM assignments WHERE id = :id")
    suspend fun getById(id: Long): Assignment?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(assignment: Assignment): Long

    @Update
    suspend fun update(assignment: Assignment)

    @Delete
    suspend fun delete(assignment: Assignment)
}
