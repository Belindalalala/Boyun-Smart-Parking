<template>
<link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css">
<div :data-theme="dataTheme" class="min-h-screen relative">
    <!-- Theme Toggle on a separate line -->
    <nav class="bg-transparent  p-4">
    <div class="flex justify-end">
        <label class="swap swap-rotate">
        <input
            type="checkbox"
            class="theme-toggle"
            @click="setDataTheme"
        />
        <svg
            class="swap-on fill-current w-6 h-6"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
        >
            <path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
        </svg>
        <svg
            class="swap-off fill-current w-6 h-6"
            xmlns="http://www.w3.org/svg"
            viewBox="0 0 24 24"
        >
            <path d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
        </svg>
        </label>
    </div>
    </nav>

    <main class="mx-auto p-4">
    <!-- New Header Section for Stats -->
    <div class="flex justify-between space-x-6 mb-6">
        <!-- Today's Income -->
        <div class="stat flex-1 text-center">
        <div class="stat-icon mb-2">
            <i class="fa fa-yen"></i>
        </div>
        <div class="stat-title text-sm">今日收入</div>
        <div class="stat-value text-lg">1200</div>
        </div>

        <!-- Total Users -->
        <div class="stat flex-1 text-center">
        <div class="stat-icon mb-2">
            <i class="fa fa-address-book-o"></i>
        </div>
        <div class="stat-title text-sm">用户总数</div>
        <div class="stat-value text-lg">1500</div>
        </div>

        <!-- Remaining Parking Spaces -->
        <div class="stat flex-1 text-center">
        <div class="stat-icon mb-2">
            <i class="fa fa-automobile"></i>
        </div>
        <div class="stat-title text-sm">剩余车位</div>
        <div class="stat-value text-lg">230</div>
        </div>

        <!-- User Records -->
        <div class="stat flex-1 text-center">
        <div class="stat-icon mb-2">
            <i class="fa fa-file-text-o"></i>
        </div>
        <div class="stat-title text-sm">停车记录</div>
        <div class="stat-value text-lg">45</div>
        </div>
    </div>

    <!-- Charts Section (Bar and Pie charts side by side with equal size) -->
    <div class="flex justify-between space-x-6">

        <div class="w-1/3 p-3">
        <!-- Parking Charge Table -->
        <section class="mb-6">
        <h2 class="text-xl font-bold text-center mb-4">停车收费规则</h2>
        <div class="overflow-x-auto">
            <table class="table-auto max-w-4xl mx-auto border-collapse border border-gray-200">
            <thead>
                <tr>
                <th class="border border-gray-300 px-6 py-3 text-center font-semibold">用户类型</th>
                <th class="border border-gray-300 px-6 py-3 text-center font-semibold">收费标准</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <td class="border border-gray-300 px-4 py-2 text-center">酒店员工</td>
                <td class="border border-gray-300 px-4 py-2 text-center">免费停车</td>
                </tr>
                <tr>
                <td class="border border-gray-300 px-4 py-2 text-center">入住客户</td>
                <td class="border border-gray-300 px-4 py-2 text-center">免费停车，超过5小时每小时10元</td>
                </tr>
                <tr>
                <td class="border border-gray-300 px-4 py-2 text-center">游客</td>
                <td class="border border-gray-300 px-4 py-2 text-center">每小时10元，超过2小时优惠5元</td>
                </tr>
                <tr>
                <td class="border border-gray-300 px-4 py-2 text-center">VIP客户</td>
                <td class="border border-gray-300 px-4 py-2 text-center">免费停车，超过10小时享受20%折扣</td>
                </tr>
                <tr>
                <td class="border border-gray-300 px-4 py-2 text-center">会员客户</td>
                <td class="border border-gray-300 px-4 py-2 text-center">免费停车，超过4小时每小时8元</td>
                </tr>
            </tbody>
            </table>
        </div>
        </section>
        </div>


        <!-- Bar Chart -->
        <div class="w-1/3 p-3">
        <h2 class="text-xl font-bold text-center mb-4">Parking Lot Occupancy (Bar Chart)</h2>
        <canvas id="barChart" width="400" height="400"></canvas>
        </div>

        <!-- Pie Chart -->
        <div class="w-1/3 p-3">
        <h2 class="text-xl font-bold text-center mb-4">Parking Lot Occupancy (Pie Chart)</h2>
        <canvas id="pieChart" width="400" height="400"></canvas>
        </div>
    </div>
    </main>

    



</div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import Chart from "chart.js/auto"; // Ensure you have Chart.js installed

const dataTheme = ref("light");
const setDataTheme = () => {
dataTheme.value = dataTheme.value === "light" ? "dark" : "light";
};

// 监听主题变化并动态修改 <html> 标签属性
watch(dataTheme, (newTheme) => {
  console.log("Theme changed to:", newTheme);
  // 只有当主题发生变化时才设置 data-theme
  if (document.documentElement.getAttribute("data-theme") !== newTheme) {
    document.documentElement.setAttribute("data-theme", newTheme);
  }
});


// 初始化主题
document.documentElement.setAttribute("data-theme", dataTheme.value);

const parkingLots = [
{ name: "Parking Lot A", capacity: 100, available: 70 },
{ name: "Parking Lot B", capacity: 150, available: 120 },
{ name: "Parking Lot C", capacity: 200, available: 150 },
{ name: "Parking Lot D", capacity: 250, available: 180 },
{ name: "Parking Lot E", capacity: 300, available: 220 }
];

onMounted(() => {
const barCtx = document.getElementById("barChart").getContext("2d");
const pieCtx = document.getElementById("pieChart").getContext("2d");

// Bar Chart
new Chart(barCtx, {
    type: "bar",
    data: {
        labels: parkingLots.map((lot) => lot.name),
        datasets: [
            {
                label: "Available Spaces",
                data: parkingLots.map((lot) => lot.available),
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1
            },
            {
                label: "Total Capacity",
                data: parkingLots.map((lot) => lot.capacity),
                backgroundColor: "rgba(153, 102, 255, 0.2)",
                borderColor: "rgba(153, 102, 255, 1)",
                borderWidth: 1
            }
        ]
    },
    options: {
        responsive: true,
        aspectRatio: 1,  // 宽高比例, 1:1.5的比例可以避免条形图过长
        scales: {
            x: { beginAtZero: true },
            y: { beginAtZero: true }
        }
    }
});


// Pie Chart
new Chart(pieCtx, {
    type: "pie",
    data: {
    labels: parkingLots.map((lot) => lot.name),
    datasets: [
        {
        data: parkingLots.map((lot) => lot.available),
        backgroundColor: [
            "rgba(75, 192, 192, 0.2)",  // Transparent color for the pie chart
            "rgba(255, 99, 132, 0.2)", 
            "rgba(255, 159, 64, 0.2)", 
            "rgba(153, 102, 255, 0.2)", 
            "rgba(54, 162, 235, 0.2)"
        ],
        borderColor: [
            "rgba(75, 192, 192, 1)", 
            "rgba(255, 99, 132, 1)", 
            "rgba(255, 159, 64, 1)", 
            "rgba(153, 102, 255, 1)", 
            "rgba(54, 162, 235, 1)"
        ],
        borderWidth: 1
        }
    ]
    },
    options: {
    responsive: true
    }
});
});
</script>

<style scoped>
/* Ensure charts are responsive and have good margins */
canvas {
margin: 0 auto;
}

/* Styling for stats above the charts */
.stat {
background-color: var(--base-100);
padding: 20px;
border-radius: 10px;
box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.stat-title {
font-size: 0.875rem; /* smaller font size */
font-weight: 600;
}

.stat-value {
font-size: 1.25rem; /* slightly smaller value */
font-weight: 700;
}

.stat-icon {
color: #4a90e2; /* Blue icon color */
}

.flex {
display: flex;
}

.justify-between {
justify-content: space-between;
}

.space-x-6 > * {
margin-right: 1.5rem;
}

.mb-2 {
margin-bottom: 0.5rem;
}
</style>
