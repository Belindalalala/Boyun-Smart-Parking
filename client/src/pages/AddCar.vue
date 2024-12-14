<template>
  <div class="my-5">
    <h2 class="text-center">新增车辆</h2>
    <div class="">
      <form
        @submit.prevent="addCar"
        class="flex flex-col justify-center items-center gap-3"
      >
        <input
          type="text"
          placeholder="车主姓名"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="car.owner_name"
        />

        <input
          type="file"
          class="file-input file-input-bordered w-full max-w-lg"
          @change="handleImageChange"
          required
        />

        <input
          type="text"
          placeholder="车牌号"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="car.license_plate"
        />
        <button class="btn btn-primary max-w-lg w-full" type="submit">
          提交
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddCar",
  data() {
    return {
      car: {
        owner_name: "",
        profile_image: null, // Corrected property name
        license_plate: "",
      },
    };
  },
  methods: {
    addCar() {
      const formData = new FormData();
      formData.append("owner_name", this.car.owner_name);
      formData.append("license_plate", this.car.license_plate);
      formData.append("profile_image", this.car.profile_image); // Corrected property name
      for (const pair of formData.entries()) {
        console.log(pair[0] + ", " + pair[1]);
      }
      fetch("http://localhost:8000/api/cars/", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to add car");
          }
          this.car = {
            name: "",
            license_plate: "",
            // profile_image: null, // Corrected property name
          };
          this.$router.push("/car");
        })
        .catch((error) => console.error("Error adding car:", error));
    },
    handleImageChange(event) {
      this.car.profile_image = event.target.files[0];
    },
  },
};
</script>

<style></style>
