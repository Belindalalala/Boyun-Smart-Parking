<template>
  <div class="p-4">
    <!-- 页面标题和新增用户按钮 -->
    <div class="flex items-center justify-between mb-4">
      <p class="text-2xl font-bold text-center">车辆管理</p>
      <button
        @click="$router.push('/car/add')"
        class="btn btn-primary"
      >
        新增车辆
      </button>
    </div>
    <!-- 表格 -->
    <div class="overflow-x-auto px-4">
      <table class="table table-auto border-collapse border border-gray-300 w-full">
        <!-- Head -->
        <thead>
          <tr class="bg-gray-200">
            <th class="px-4 py-2 border">ID</th>
            <th class="px-4 py-2 border">Profile Image</th>
            <th class="px-4 py-2 border">License plate</th>
            <th class="px-4 py-2 border">Owner Name</th>
            <th class="px-4 py-2 border">Options</th>
          </tr>
        </thead>
        <tbody>
          <!-- Rows -->
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-100">
            <td class="px-4 py-2 border">{{ user.id }}</td>
            <td class="px-4 py-2 border">
              <div class="avatar">
                <div class="w-16 rounded-full">
                  <img :src="user.profile_image" />
                </div>
              </div>
            </td>
            <td class="px-4 py-2 border">{{ user.license_plate }}</td>
            <td class="px-4 py-2 border">{{ user.owner_name }}</td>
            <td class="px-4 py-2 border">
              <div class="flex gap-3 justify-center">
                <button class="btn btn-circle w-fit" @click="updateUser(user.id)">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth="{1.5}"
                    stroke="currentColor"
                    class="w-6 h-6"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M16.862 4.487l1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931ZM16.862 4.487L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10"
                    />
                  </svg>
                </button>
                <button @click="deleteUser(user.id)" class="btn btn-circle w-fit">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth="{1.5}"
                    stroke="currentColor"
                    class="w-6 h-6"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M15 12H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
                    />
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <!-- End of Rows -->
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "ViewCar",
  data() {
    return {
      users: [],
    };
  },
  methods: {
    fetchUsers() {
      fetch("http://localhost:8000/api/cars/")
        .then((res) => res.json())
        .then((data) => (this.users = data))
        .catch((error) => console.error("Error fetching users:", error));
    },
    updateUser(id) {
      this.$router.push(`/car/update/${id}`);
    },
    deleteUser(id) {
      fetch(`http://localhost:8000/api/cars/${id}`, {
        method: "DELETE",
      }).then(() => this.fetchUsers());
    },
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>

<style>
/* 添加必要的表格样式 */
.table th,
.table td {
  text-align: left;
}
</style>
