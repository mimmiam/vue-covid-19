<template>
  <div>
    <v-col>
        <v-row class="justify-end green-25">
          <div class="text-h4 mr-2 font-weight-bold">+{{Number(ReceivedTreatment.case_new).toLocaleString()}}</div>
        </v-row>
        <v-row class="justify-center green-25">
          <div class="text-h1 mt-2 font-weight-bold">{{Number(ReceivedTreatment.case_total).toLocaleString()}}</div>
        </v-row>
        <v-row class="justify-end green-25">
          <div class="text-h4 mt-n4 mr-2 font-weight-bold">ราย</div>
        </v-row>
      <v-row>
        <v-col class="pa-6 green-75">
          <v-row class="justify-center">
            <div class="text-h6">ผู้ป่วยรักษาอยู่</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(ReceivedTreatment.case_in_treatment).toLocaleString()}}</div>
          </v-row>
        </v-col>
        <v-col class="pa-6 green-50">
          <v-row class="justify-center">
            <div class="text-h6">ร้อยละ</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(ReceivedTreatment.percentage).toLocaleString()}}</div>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </div>
</template>

<script>
export default {
  name: 'getWell',
  data: () => ({
  }),
  props: {
    ReceivedTreatment: {
      type: Object
    }
  }
}
</script>

<style scoped>
.green-25{
    background-color: rgb(165, 180, 81);
    color: #ffffff;
}
.green-50{
    background-color: rgb(126,146,63);
    color: #ffffff;
}
.green-75{
    background-color: rgb(86,112,52);
    color: #ffffff;
}
</style>
