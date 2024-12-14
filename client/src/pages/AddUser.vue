<template>
  <div class="my-5">
    <h2 class="text-center">新增用户</h2>
    <div class="">
      <form
        @submit.prevent="addUser"
        class="flex flex-col justify-center items-center gap-3"
      >
        <!-- 姓名输入框 -->
        <input
          type="text"
          placeholder="姓名"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="user.name"
        />

        <!-- 电话号码输入框 -->
        <input
          type="tel"
          placeholder="电话号码"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="user.phone"
        />

        <!-- 身份选择框 -->
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
          提交
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddUser",
  data() {
    return {
      user: {
        name: "",
        phone: "",
        status: "", // 用户身份
      },
    };
  },
  methods: {
    addUser() {
      const formData = new FormData();
      formData.append("name", this.user.name);
      formData.append("phone", this.user.phone);
      formData.append("status", this.user.status);

      // 打印表单数据（调试时查看）
      for (const pair of formData.entries()) {
        console.log(pair[0] + ", " + pair[1]);
      }

      fetch("http://localhost:8000/api/users/", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to add user");
          }
          this.user = {
            name: "",
            phone: "",
            status: "", // 重置表单
          };
          this.$router.push("/user"); // 跳转回用户列表页
        })
        .catch((error) => console.error("Error adding user:", error));
    },
  },
};
</script>

<style>
</style>
