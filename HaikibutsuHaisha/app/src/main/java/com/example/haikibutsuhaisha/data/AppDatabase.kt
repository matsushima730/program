package com.example.haikibutsuhaisha.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.TypeConverter
import androidx.room.TypeConverters
import com.example.haikibutsuhaisha.data.dao.AssignmentDao
import com.example.haikibutsuhaisha.data.dao.ClientDao
import com.example.haikibutsuhaisha.data.dao.DriverDao
import com.example.haikibutsuhaisha.data.dao.TruckDao
import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.BodyType
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import com.example.haikibutsuhaisha.data.entity.ContainerStatus
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.entity.Truck

class Converters {
    @TypeConverter fun bodyToString(v: BodyType?): String? = v?.name
    @TypeConverter fun stringToBody(v: String?): BodyType? = v?.let { BodyType.fromName(it) }

    @TypeConverter fun kindToString(v: ClientKind?): String? = v?.name
    @TypeConverter fun stringToKind(v: String?): ClientKind? = v?.let { runCatching { ClientKind.valueOf(it) }.getOrNull() }

    @TypeConverter fun statusToString(v: ContainerStatus?): String? = v?.name
    @TypeConverter fun stringToStatus(v: String?): ContainerStatus? = v?.let { ContainerStatus.fromName(it) }
}

@Database(
    entities = [Truck::class, Driver::class, Client::class, Assignment::class],
    version = 1,
    exportSchema = false
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun truckDao(): TruckDao
    abstract fun driverDao(): DriverDao
    abstract fun clientDao(): ClientDao
    abstract fun assignmentDao(): AssignmentDao

    companion object {
        @Volatile private var instance: AppDatabase? = null

        fun get(context: Context): AppDatabase = instance ?: synchronized(this) {
            instance ?: Room.databaseBuilder(
                context.applicationContext,
                AppDatabase::class.java,
                "haikibutsu.db"
            ).build().also { instance = it }
        }
    }
}
