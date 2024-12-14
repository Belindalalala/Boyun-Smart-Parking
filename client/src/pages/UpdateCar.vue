<template>
  <div>
    <h2>Update Car</h2>
    <div>
      <form @submit.prevent="updateCar" class="flex flex-col justify-center items-center gap-3">

        <input
          type="text"
          placeholder="owner_name"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="car.owner_name"
        />
 
        <!-- <div class="w-32">
          <img :src="car.profile_image" :key="car.profile_image" />
        </div>
 
        <input
          type="file"
          class="file-input file-input-bordered w-full max-w-lg"
          @change="handleImageChange"
        /> -->
 
        <input
          type="text"
          placeholder="license_plate"
          class="input input-bordered w-full max-w-lg"
          required
          v-model="car.license_plate"
        />
        <button class="btn btn-primary max-w-lg w-full" type="submit">
          Submit
        </button>
      </form>
    </div>
  </div>
 </template>
 
 <script>
 export default {
  name: "UpdateCar",
  data() {
    return {
      id: 0,
      // newImage: null,
      car: {
        id: 0,
        owner_name: "",
        // profile_image: null,
        license_plate: "",
      },
    };
  },
  methods: {
    // imageUrlToObjectFile(imageUrl) {
    //   return new Promise((resolve, reject) => {
    //     fetch(imageUrl)
    //       .then((response) => response.blob())
    //       .then((blob) => {
    //         const file = new File([blob], "image.jpg", { type: "image/jpeg" });
    //         resolve(file);
    //       })
    //       .catch((error) => {
    //         reject(error);
    //       });
    //   });
    // },
    async fetchCar() {
      try {
        const response = await fetch(
          `http://localhost:8000/api/cars/${this.$route.params.id}/`
        );
        const data = await response.json();
        if (response.ok) {
          this.car = data;
          // if (this.car.profile_image) {
          //   const file = await this.imageUrlToObjectFile(this.car.profile_image);
          //   this.car.profile_image = file;
          // }
        } else {
          console.error("Failed to fetch car data");
        }
      } catch (error) {
        console.error(error);
      }
    },
    // handleImageChange(event) {
    //   const file = event.target.files[0];
    //   this.newImage = file;
    //   if (file) {
    //     const reader = new FileReader();
    //     reader.onload = () => {
    //       this.car.profile_image = reader.result;
    //     };
    //     reader.readAsDataURL(file);
    //   } else {
    //     this.car.profile_image = null;
    //   }
    // },
    async updateCar() {
      const carData = {
        owner_name: this.car.owner_name,
        license_plate: this.car.license_plate,
        // profile_image: this.newImage,
      };

      console.log("Submitting car data:", carData);  // 打印提交的数据

      try {
        const response = await fetch(`http://localhost:8000/api/cars/${this.car.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json; charset=UTF-8",  // 指定 UTF-8 编码
          },
          body: JSON.stringify(carData),  // 传递 JSON 格式数据
        });

        if (response.ok) {
          this.car = {
            id: 0,
            owner_name: "",
            license_plate: "",
            // profile_image: null,
          };
          this.$router.push("/car");  // 跳转到首页
        } else {
          throw new Error("Failed to update car");
        }
      } catch (error) {
        console.error("Error updating car:", error);
      }
    },
  },
  mounted() {
    this.fetchCar();
  },
 };
 </script>
 
 <style scoped>
 /* 可以根据需要添加样式 */
 </style>