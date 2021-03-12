<template>
  <div>
    <v-col>
      <v-row class="justify-center blue-25">
        <div class="text-h1 mt-2 font-weight-bold">+{{Number(PatientToDay.case_new).toLocaleString()}}</div>
      </v-row>
      <v-row class="justify-end blue-25">
        <div class="text-h4 mt-n4 mr-2 font-weight-bold">ราย</div>
      </v-row>
      <v-row class="purple-50">
        <v-col cols="10">
          <div class="text-h6">ผู้ป่วยรายใหม่จากระบบเฝ้าระวังและระบบบริการฯ</div>
        </v-col>
        <v-col cols="2" align="right">
          <div class="text-h4 font-weight-bold">{{Number(PatientToDay.case_infected_check_point).toLocaleString()}}</div>
        </v-col>
      </v-row>
      <v-row class="purple-25">
        <v-col cols="10">
          <div class="text-h6">ค้นหาผู้ติดเชื้อเชิงรุกในชุมชน</div>
        </v-col>
        <v-col cols="2" align="right">
          <div class="text-h4 font-weight-bold">{{Number(PatientToDay.case_infected_community).toLocaleString()}}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col align="center" class="pa-6 blue-75">
          <v-row>
            <div class="text-h6">ผู้เดินทางจากต่างประเทศไม่เข้าสถานที่กักกัน</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(PatientToDay.case_from_foreign_no_q).toLocaleString()}}</div>
          </v-row>
        </v-col>
        <v-col align="center" class="pa-6 blue-50" style="height:8rem;">
          <v-row>
            <div class="text-h6">ผู้เดินทางจากต่างประเทศเข้าสถานที่กักกันที่รัฐจัดให้</div>
          </v-row>
          <v-row class="justify-center">
            <div class="text-h4 font-weight-bold">{{Number(PatientToDay.case_from_foreign_in_q).toLocaleString()}}</div>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </div>
</template>

<script>
export default {
  name: 'patientNow',
  data: () => ({
  }),
  props: {
    PatientToDay: {
      type: Object
    }
  }
  // created () {
  //   console.log('dd', this.PatientToDay)
  // }
  // props: ['PatientToDay']
}
</script>

<style scoped>
.blue-25{
    background-color: rgb(67,154,212);
    color: #ffffff;
}
.blue-50{
    background-color: rgb(47,117,184);
    color: #ffffff;
}
.blue-75{
    background-color: rgb(28,79,153);
    color: #ffffff;
}
.purple-50{
    background-color: rgb(49,59,141);
    color: #ffffff;
}
.purple-25{
    background-color: rgb(88,109,211);
    color: #ffffff;
}
</style>
