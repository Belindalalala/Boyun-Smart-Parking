<template>
    <div>
      <h2>Update Record</h2>
      <div>
        <form
          @submit.prevent="updatePark"
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
    name: "UpdateCar",
    data() {
      return {
        id: 0,
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
      async fetchPark() {
        try {
          const response = await fetch(
            `http://localhost:8000/api/parks/${this.$route.params.id}/`
          );
          const data = await response.json();
          if (response.ok) {
            this.park = data;
          } else {
            console.error("Failed to fetch park data");
          }
        } catch (error) {
          console.error(error);
        }
      },
      async updatePark() {
        const formData = new FormData();
        formData.append("license_plate", this.park.license_plate);
        formData.append("parking_area", this.park.parking_area);
        formData.append("parking_number", this.park.parking_number); 
        formData.append("entry_time", this.park.entry_time);
        formData.append("exit_time", this.park.exit_time);
        formData.append("fee", this.park.fee);
   
        fetch(`http://localhost:8000/api/parks/${this.park.id}/`, {
          method: "PUT",
          body: formData,
        })
          .then((response) => {
            if (response.ok) {
              this.park = {
              license_plate: "",
              parking_area: "",
              parking_number: "", // Corrected property name
              entry_time: "",
              exit_time: "",
              fee: "",
              };
              this.$router.push("/record");
            } else {
              throw new Error("Failed to update park");
            }
          })
          .catch((error) => console.error("Error updating park:", error));
      },
    },
    mounted() {
      this.fetchPark();
    },
   };
   </script>
   
   <style></style>