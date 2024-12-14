<template>
  <div>
    <h2>Update User</h2>
    <div>
      <form @submit.prevent="updateUser" class="flex flex-col justify-center items-center gap-3">
        <!-- 用户姓名 -->
        <input
          type="text"
          placeholder="name"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="user.name"
        />
        
        <!-- 用户电话号码 -->
        <input
          type="tel"
          placeholder="phone"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="user.phone"
        />
        
        <!-- 用户身份 -->
        <select 
          v-model="user.status" 
          class="input input-bordered w-full max-w-lg" 
          required
        >
          <option disabled value="">请选择身份</option>
          <option value="HOTEL_STAFF">HOTEL_STAFF</option>
          <option value="VIP">VIP</option>
          <option value="SVIP">SVIP</option>
          <option value="GUEST">GUEST</option>
          <option value="VISITOR">VISITOR</option>
        </select>
        
        <!-- 提交按钮 -->
        <button class="btn btn-primary max-w-lg w-full" type="submit">
          Submit
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "UpdateUser",
  data() {
    return {
      id: 0,
      user: {
        id: 0,
        name: "",
        phone: "",
        status: "",
      },
    };
  },
  methods: {
    // 获取用户信息
    async fetchUser() {
      try {
        const response = await fetch(
          `http://localhost:8000/api/users/${this.$route.params.id}/`
        );
        const data = await response.json();
        if (response.ok) {
          this.user = data; // 填充用户数据
        } else {
          console.error("Failed to fetch user data");
        }
      } catch (error) {
        console.error(error);
      }
    },

    // 更新用户信息
    async updateUser() {
      const userData = {
        name: this.user.name,
        phone: this.user.phone,
        status: this.user.status,
      };

      console.log("Submitting user data:", userData);  // 打印提交的数据

      try {
        const response = await fetch(`http://localhost:8000/api/users/${this.user.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json; charset=UTF-8",  // 指定 UTF-8 编码
          },
          body: JSON.stringify(userData),  // 传递 JSON 格式数据
        });

        if (response.ok) {
          this.user = {
            id: 0,
            name: "",
            phone: "",
            status: "",
          };
          this.$router.push("/user");  // 跳转到首页
        } else {
          throw new Error("Failed to update user");
        }
      } catch (error) {
        console.error("Error updating user:", error);
      }
    },
  },
  mounted() {
    this.fetchUser();  // 在组件加载时获取用户信息
  },
};
</script>

<style scoped>
/* 可以根据需要添加样式 */
</style>
