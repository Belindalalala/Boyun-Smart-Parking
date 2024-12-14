<template>
    <div class="my-5">
      <h2 class="text-center">新增记录</h2>
      <div class="">
        <form
          @submit.prevent="addPark"
          class="flex flex-col justify-center items-center gap-3"
        >
          <input
            type="text"
            placeholder="license_plate"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.license_plate"
          />
  
          <input
            type="text"
            placeholder="parking_area"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.parking_area"
          />
  
          <input
            type="text"
            placeholder="parking_number"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.parking_number"
          />

          <input
            type="datetime-local"
            placeholder="entry_time"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.entry_time"
          />

          <input
            type="datetime-local"
            placeholder="exit_time"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.exit_time"
          />

          <input
            type="text"
            placeholder="fee"
            class="input input-bordered w-full max-w-lg"
            required
            v-model="park.fee"
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
    name: "AddPark",
    data() {
      return {
        park: {
          license_plate: "",
          parking_area: "",
          parking_number: "", 
          entry_time: 0,
          exit_time: 0,
          fee: 0,
        },
      };
    },
    methods: {
      addPark() {
        const formData = new FormData();
        formData.append("license_plate", this.park.license_plate);
        formData.append("parking_area", this.park.parking_area);
        formData.append("parking_number", this.park.parking_number); 
        formData.append("entry_time", this.park.entry_time);
        formData.append("exit_time", this.park.exit_time);
        formData.append("fee", this.park.fee);
        for (const pair of formData.entries()) {
          console.log(pair[0] + ", " + pair[1]);
        }
        fetch("http://localhost:8000/api/parks/", {
          method: "POST",
          body: formData,
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error("Failed to add park");
            }
            this.park = {
              license_plate: "",
              parking_area: "",
              parking_number: "", // Corrected property name
              entry_time: "",
              exit_time: "",
              fee: "",
            };
            this.$router.push("/record");
          })
          .catch((error) => console.error("Error adding park:", error));
      },
      // handleImageChange(event) {
      //   this.park.profile_image = event.target.files[0];
      // },
    },
  };
  </script>
  
  <style></style>
  