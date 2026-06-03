package com.example.haikibutsuhaisha.ui.nav

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.CalendarMonth
import androidx.compose.material.icons.outlined.Business
import androidx.compose.material.icons.outlined.LocalShipping
import androidx.compose.material.icons.outlined.Person
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.navArgument
import com.example.haikibutsuhaisha.ui.calendar.AssignmentEditScreen
import com.example.haikibutsuhaisha.ui.calendar.CalendarScreen
import com.example.haikibutsuhaisha.ui.client.ClientEditScreen
import com.example.haikibutsuhaisha.ui.client.ClientListScreen
import com.example.haikibutsuhaisha.ui.driver.DriverEditScreen
import com.example.haikibutsuhaisha.ui.driver.DriverListScreen
import com.example.haikibutsuhaisha.ui.truck.TruckEditScreen
import com.example.haikibutsuhaisha.ui.truck.TruckListScreen

sealed class Dest(val route: String) {
    data object Calendar : Dest("calendar")
    data object Trucks : Dest("trucks")
    data object Drivers : Dest("drivers")
    data object Clients : Dest("clients")

    data object AssignmentEdit : Dest("assignment/{date}/{id}") {
        fun build(date: String, id: Long) = "assignment/$date/$id"
    }
    data object TruckEdit : Dest("truck/{id}") {
        fun build(id: Long) = "truck/$id"
    }
    data object DriverEdit : Dest("driver/{id}") {
        fun build(id: Long) = "driver/$id"
    }
    data object ClientEdit : Dest("client/{id}") {
        fun build(id: Long) = "client/$id"
    }
}

private data class BottomItem(val dest: Dest, val label: String, val icon: ImageVector)

private val bottomItems = listOf(
    BottomItem(Dest.Calendar, "配車", Icons.Outlined.CalendarMonth),
    BottomItem(Dest.Trucks, "車両", Icons.Outlined.LocalShipping),
    BottomItem(Dest.Drivers, "ドライバー", Icons.Outlined.Person),
    BottomItem(Dest.Clients, "取引先", Icons.Outlined.Business)
)

@Composable
fun AppBottomBar(nav: NavHostController) {
    val backStack by nav.currentBackStackEntryAsState()
    val current = backStack?.destination
    NavigationBar {
        bottomItems.forEach { item ->
            val selected = current?.hierarchy?.any { it.route == item.dest.route } == true
            NavigationBarItem(
                selected = selected,
                onClick = {
                    nav.navigate(item.dest.route) {
                        popUpTo(nav.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                },
                icon = { Icon(item.icon, contentDescription = item.label) },
                label = { Text(item.label) }
            )
        }
    }
}

@Composable
fun AppNavHost(nav: NavHostController, modifier: Modifier = Modifier) {
    NavHost(navController = nav, startDestination = Dest.Calendar.route, modifier = modifier) {
        composable(Dest.Calendar.route) {
            CalendarScreen(
                onEditAssignment = { date, id -> nav.navigate(Dest.AssignmentEdit.build(date, id)) }
            )
        }
        composable(Dest.Trucks.route) {
            TruckListScreen(onEdit = { id -> nav.navigate(Dest.TruckEdit.build(id)) })
        }
        composable(Dest.Drivers.route) {
            DriverListScreen(onEdit = { id -> nav.navigate(Dest.DriverEdit.build(id)) })
        }
        composable(Dest.Clients.route) {
            ClientListScreen(onEdit = { id -> nav.navigate(Dest.ClientEdit.build(id)) })
        }

        composable(
            Dest.AssignmentEdit.route,
            arguments = listOf(
                navArgument("date") { type = NavType.StringType },
                navArgument("id")   { type = NavType.LongType }
            )
        ) { backStackEntry ->
            val date = backStackEntry.arguments?.getString("date").orEmpty()
            val id = backStackEntry.arguments?.getLong("id") ?: 0L
            AssignmentEditScreen(date = date, assignmentId = id, onDone = { nav.popBackStack() })
        }
        composable(Dest.TruckEdit.route, arguments = listOf(navArgument("id") { type = NavType.LongType })) {
            val id = it.arguments?.getLong("id") ?: 0L
            TruckEditScreen(id = id, onDone = { nav.popBackStack() })
        }
        composable(Dest.DriverEdit.route, arguments = listOf(navArgument("id") { type = NavType.LongType })) {
            val id = it.arguments?.getLong("id") ?: 0L
            DriverEditScreen(id = id, onDone = { nav.popBackStack() })
        }
        composable(Dest.ClientEdit.route, arguments = listOf(navArgument("id") { type = NavType.LongType })) {
            val id = it.arguments?.getLong("id") ?: 0L
            ClientEditScreen(id = id, onDone = { nav.popBackStack() })
        }
    }
}
