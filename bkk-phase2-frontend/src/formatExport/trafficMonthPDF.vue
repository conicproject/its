<template>
  <div>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="false"
      :preview-modal="false"
      :paginate-elements-by-height="1400"
      filename="test"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a3"
      pdf-orientation="landscape"
      pdf-content-width="100%"
      ref="html2Pdfmonth"
      :pdf-margin="10"
    >
      <section slot="pdf-content">
        <!-- <table
          id="mytableX_month"
          data-cols-width="20,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,15"
        > -->
        <table
          id="mytableX_month"
        >
          <tr>
            <th colspan="33" data-f-sz="25" data-a-h="right" data-f-bold="true">
              กองระบบเทคโนโลยีจราจร
            </th>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th>
                      <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
          </tr>
          <tr>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
            <th colspan="33" data-f-sz="25" data-a-h="right" data-f-bold="true">
              สำนักการจราจรและขนส่ง กรุงเทพมหานคร
            </th>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กรุงเทพมหานคร</th> -->
          </tr>
          <tr></tr>
          <tr>
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">กองระบบเทคโนโลยีจราจร </th> -->
            <!-- <th colspan="8" data-f-sz="20"  data-a-h="center"  data-f-bold="true">สำนักการจราจรและขนส่ง </th> -->
            <th colspan="33" data-f-sz="25" data-a-h="left" data-f-bold="true">
              รายงานปริมาณจราจรแยกตามประเภทยานพาหนะ(รายเดือน)
            </th>
          </tr>

          <tr></tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">
              จุดติดตั้ง {{ nameCheckPoint }}
            </th>
          </tr>

          <tr></tr>
          <tr>

            <th colspan="25" data-f-sz="25" data-a-h="left" data-f-bold="true">
              เดือน/ปี {{ dateText }}
            </th>
          </tr>

          <tr></tr>
          <tr>
            <th data-f-sz="15">
              ปริมาณจราจรรายเดือน (ทิศทางการจราจรเข้าเมือง) (คัน)
            </th>
          </tr>
          <tr v-if="checkMonth === 0 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 0 && dataKey.keyCard == 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard === 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard === 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.type">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.type }}
            </td>
            <td
              v-if="item._0 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._0 }}
            </td>
            <td
              v-if="item._1 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._1 }}
            </td>
            <td
              v-if="item._2 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._2 }}
            </td>
            <td
              v-if="item._3 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._3 }}
            </td>
            <td
              v-if="item._4 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._4 }}
            </td>
            <td
              v-if="item._5 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._5 }}
            </td>
            <td
              v-if="item._6 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._6 }}
            </td>
            <td
              v-if="item._7 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._7 }}
            </td>
            <td
              v-if="item._8 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._8 }}
            </td>
            <td
              v-if="item._9 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._9 }}
            </td>
            <td
              v-if="item._10 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._10 }}
            </td>
            <td
              v-if="item._11 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._11 }}
            </td>
            <td
              v-if="item._12 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._12 }}
            </td>
            <td
              v-if="item._13 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._13 }}
            </td>
            <td
              v-if="item._14 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._14 }}
            </td>
            <td
              v-if="item._15 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._15 }}
            </td>
            <td
              v-if="item._16 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._16 }}
            </td>
            <td
              v-if="item._17 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._17 }}
            </td>
            <td
              v-if="item._18 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._18 }}
            </td>
            <td
              v-if="item._19 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._19 }}
            </td>
            <td
              v-if="item._20 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._20 }}
            </td>
            <td
              v-if="item._21 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._21 }}
            </td>
            <td
              v-if="item._22 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._22 }}
            </td>
            <td
              v-if="item._23 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._23 }}
            </td>
            <td
              v-if="item._24 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._24 }}
            </td>
            <td
              v-if="item._25 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._25 }}
            </td>
            <td
              v-if="item._26 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._26 }}
            </td>
            <td
              v-if="item._27 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._27 }}
            </td>
            <td
              v-if="item._28 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._28 }}
            </td>
            <td
              v-if="item._29 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._29 }}
            </td>
            <td
              v-if="item._30 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._30 }}
            </td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.all }}
            </td>

            <td
              v-if="item.percent !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item.percent }}
            </td>
          </tr>
          <tr></tr>
          <tr></tr>
          <tr></tr>
          <tr>
            <th data-f-sz="15">
              ปริมาณจราจรรายเดือน (ทิศทางการจราจรออกเมือง) (คัน)
            </th>
          </tr>
          <tr v-if="checkMonth === 0 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 0 && dataKey.keyCard == 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard === 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard !== 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard === 'violate'">
            <th
              data-a-h="center"
              data-f-sz="15"
              v-for="item in headerTable"
              :key="item"
            >
              {{ item }}
            </th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.id">
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.type }}
            </td>
            <td
              v-if="item._0 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._0 }}
            </td>
            <td
              v-if="item._1 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._1 }}
            </td>
            <td
              v-if="item._2 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._2 }}
            </td>
            <td
              v-if="item._3 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._3 }}
            </td>
            <td
              v-if="item._4 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._4 }}
            </td>
            <td
              v-if="item._5 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._5 }}
            </td>
            <td
              v-if="item._6 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._6 }}
            </td>
            <td
              v-if="item._7 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._7 }}
            </td>
            <td
              v-if="item._8 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._8 }}
            </td>
            <td
              v-if="item._9 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._9 }}
            </td>
            <td
              v-if="item._10 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._10 }}
            </td>
            <td
              v-if="item._11 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._11 }}
            </td>
            <td
              v-if="item._12 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._12 }}
            </td>
            <td
              v-if="item._13 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._13 }}
            </td>
            <td
              v-if="item._14 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._14 }}
            </td>
            <td
              v-if="item._15 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._15 }}
            </td>
            <td
              v-if="item._16 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._16 }}
            </td>
            <td
              v-if="item._17 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._17 }}
            </td>
            <td
              v-if="item._18 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._18 }}
            </td>
            <td
              v-if="item._19 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._19 }}
            </td>
            <td
              v-if="item._20 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._20 }}
            </td>
            <td
              v-if="item._21 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._21 }}
            </td>
            <td
              v-if="item._22 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._22 }}
            </td>
            <td
              v-if="item._23 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._23 }}
            </td>
            <td
              v-if="item._24 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._24 }}
            </td>
            <td
              v-if="item._25 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._25 }}
            </td>
            <td
              v-if="item._26 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._26 }}
            </td>
            <td
              v-if="item._27 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._27 }}
            </td>
            <td
              v-if="item._28 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._28 }}
            </td>
            <td
              v-if="item._29 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._29 }}
            </td>
            <td
              v-if="item._30 !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item._30 }}
            </td>
            <td data-a-h="center" data-b-a-s="thin" data-f-sz="15">
              {{ item.all }}
            </td>
            <td
              v-if="item.percent !== undefined"
              data-a-h="center"
              data-b-a-s="thin"
              data-f-sz="15"
            >
              {{ item.percent }}
            </td>
          </tr>
        </table>

        <table id="mytableM1">
          <tr v-if="checkMonth === 0 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 0 && dataKey.keyCard == 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-for="item in dataInbound" :key="item.id">
            <td>{{ item.type }}</td>
            <td v-if="item._0 !== undefined">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined">{{ item._11 }}</td>
            <td v-if="item._12 !== undefined">{{ item._12 }}</td>
            <td v-if="item._13 !== undefined">{{ item._13 }}</td>
            <td v-if="item._14 !== undefined">{{ item._14 }}</td>
            <td v-if="item._15 !== undefined">{{ item._15 }}</td>
            <td v-if="item._16 !== undefined">{{ item._16 }}</td>
            <td v-if="item._17 !== undefined">{{ item._17 }}</td>
            <td v-if="item._18 !== undefined">{{ item._18 }}</td>
            <td v-if="item._19 !== undefined">{{ item._19 }}</td>
            <td v-if="item._20 !== undefined">{{ item._20 }}</td>
            <td v-if="item._21 !== undefined">{{ item._21 }}</td>
            <td v-if="item._22 !== undefined">{{ item._22 }}</td>
            <td v-if="item._23 !== undefined">{{ item._23 }}</td>
            <td v-if="item._24 !== undefined">{{ item._24 }}</td>
            <td v-if="item._25 !== undefined">{{ item._25 }}</td>
            <td v-if="item._26 !== undefined">{{ item._26 }}</td>
            <td v-if="item._27 !== undefined">{{ item._27 }}</td>
            <td v-if="item._28 !== undefined">{{ item._28 }}</td>
            <td v-if="item._29 !== undefined">{{ item._29 }}</td>
            <td v-if="item._30 !== undefined">{{ item._30 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>
          </tr>
        </table>

        <table id="mytableM2">
          <tr v-if="checkMonth === 0 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 0 && dataKey.keyCard == 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 1 && dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard !== 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-else-if="checkMonth === 2 && dataKey.keyCard === 'violate'">
            <th v-for="item in headerTable" :key="item">{{ item }}</th>
          </tr>
          <tr v-for="item in dataOutbound" :key="item.id">
            <td>{{ item.type }}</td>
            <td v-if="item._0 !== undefined">{{ item._0 }}</td>
            <td v-if="item._1 !== undefined">{{ item._1 }}</td>
            <td v-if="item._2 !== undefined">{{ item._2 }}</td>
            <td v-if="item._3 !== undefined">{{ item._3 }}</td>
            <td v-if="item._4 !== undefined">{{ item._4 }}</td>
            <td v-if="item._5 !== undefined">{{ item._5 }}</td>
            <td v-if="item._6 !== undefined">{{ item._6 }}</td>
            <td v-if="item._7 !== undefined">{{ item._7 }}</td>
            <td v-if="item._8 !== undefined">{{ item._8 }}</td>
            <td v-if="item._9 !== undefined">{{ item._9 }}</td>
            <td v-if="item._10 !== undefined">{{ item._10 }}</td>
            <td v-if="item._11 !== undefined">{{ item._11 }}</td>
            <td v-if="item._12 !== undefined">{{ item._12 }}</td>
            <td v-if="item._13 !== undefined">{{ item._13 }}</td>
            <td v-if="item._14 !== undefined">{{ item._14 }}</td>
            <td v-if="item._15 !== undefined">{{ item._15 }}</td>
            <td v-if="item._16 !== undefined">{{ item._16 }}</td>
            <td v-if="item._17 !== undefined">{{ item._17 }}</td>
            <td v-if="item._18 !== undefined">{{ item._18 }}</td>
            <td v-if="item._19 !== undefined">{{ item._19 }}</td>
            <td v-if="item._20 !== undefined">{{ item._20 }}</td>
            <td v-if="item._21 !== undefined">{{ item._21 }}</td>
            <td v-if="item._22 !== undefined">{{ item._22 }}</td>
            <td v-if="item._23 !== undefined">{{ item._23 }}</td>
            <td v-if="item._24 !== undefined">{{ item._24 }}</td>
            <td v-if="item._25 !== undefined">{{ item._25 }}</td>
            <td v-if="item._26 !== undefined">{{ item._26 }}</td>
            <td v-if="item._27 !== undefined">{{ item._27 }}</td>
            <td v-if="item._28 !== undefined">{{ item._28 }}</td>
            <td v-if="item._29 !== undefined">{{ item._29 }}</td>
            <td v-if="item._30 !== undefined">{{ item._30 }}</td>
            <td>{{ item.all }}</td>
            <td v-if="item.percent !== undefined">{{ item.percent }}</td>
          </tr>
        </table>
      </section>
    </vue-html2pdf>
    <!-- <v-btn @click="generateReport">download</v-btn> -->
  </div>
</template>
<script>
import { jsPDF } from "jspdf";
import fontTH from "../fontTH.js";
import VueHtml2pdf from "vue-html2pdf";
import VueApexCharts from "vue-apexcharts";
import "jspdf-autotable";
import TableToExcel from "@linways/table-to-excel";
import THSarabunNewBold from "../THSarabunNewBold.js";
export default {
  props: [
    "downloadpdf",
    "downloadexcel",
    "exportAdmin",
    "dataInbound",
    "dataOutbound",
    "dateText",
    "nameCheckPoint",
    "checkMonth",
    "textHeaderReport",
    "dataKey",
    "headerTable",
  ],
  components: {
    VueHtml2pdf,
    apexchart: VueApexCharts,
  },
  watch: {
    downloadpdf: function (newVal, oldVal) {
      // watch it
      this.genPDF();
      // console.log('pdf', this.headerTable);
    },
    downloadexcel: function (newVal, oldVal) {
      // watch it

      // this.generateReport();
      this.genExcel();
    },
  },
  data() {
    return {
      textCheckPoint: "",
    };
  },
  methods: {
    genExcel() {
      TableToExcel.convert(document.getElementById("mytableX_month"), {
        name: "รายงานผลข้อมูลจราจรแยกตามประเภทยานพาหนะ(รายเดือน).xlsx",
        sheet: {
          name: "Sheet 1",
        },
      });
    },
    generateReport() {
      this.$refs.html2Pdfmonth.generatePdf();
    },

    genPDF() {
      let doc = new jsPDF({ orientation: "l", unit: "pt", compress: true });
      this.textCheckPoint = this.nameCheckPoint || "";
      doc.addFileToVFS("THSarabunNew.ttf", fontTH.th);

      doc.addFileToVFS("THSarabunNew-bold.ttf", THSarabunNewBold.font);
      doc.addFont("THSarabunNew-bold.ttf", "THSarabunNewBold", "bold");
      doc.addFont("THSarabunNew.ttf", "THSarabunNew", "bold");
      doc.setFont("THSarabunNew", "bold");
      doc.setFontSize(20);
      doc.setFont("THSarabunNewBold", "bold");
      doc.text(this.textHeaderReport, 170, 45);
      doc.text("จุดติดตั้ง " + this.textCheckPoint, 170, 90);
      doc.text("เดือน/ปี " + this.dateText, 170, 110);
      doc.setFontSize(24);
      doc.text("กองระบบเทคโนโลยีจราจร", 560, 50);
      doc.text("สำนักการจราจรและขนส่ง กรุงเทพมหานคร", 510, 75);
      doc.setFontSize(16);
      doc.text("ปริมาณจราจรในแต่ละวัน (ขาเข้า) (คัน)", 40, 150);
      const logo = require("@/assets/img/BMALogo3.jpg");

      var imgLogo = new Image();
      imgLogo.src = logo;
      // // console.log("logo", this.imgURL);
      doc.addImage(imgLogo, "JPEG", 40, 20, 100, 100, undefined, "FAST");


      doc.text("ปริมาณจราจรในแต่ละวัน (ขาออก) (คัน)", 40, 350);


      doc.autoTable({
        html: "#mytableM1",
        startY: 155,
        styles: {
          font: "THSarabunNew",
          fontSize: 8,
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: {
          fillColor: [255, 255, 255],
          lineColor: [0, 0, 0],
          textColor: [0, 0, 0],
          lineWidth: 1,
        },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.autoTable({
        html: "#mytableM2",
        startY: 355,
        styles: {
          font: "THSarabunNew",
          fontSize: 8,
          halign: "center",
          overflow: "linebreak",
          cellWidth: "auto",
          fontSize: 8,
          textColor: "#000",
          cellPadding: 1,
        },
        theme: "grid",
        headStyles: {
          fillColor: [255, 255, 255],
          lineColor: [0, 0, 0],
          textColor: [0, 0, 0],
          lineWidth: 1,
        },
        bodyStyles: { fillColor: [255, 255, 255], lineColor: [0, 0, 0] },
      });

      doc.save(`รายงานเดือน.pdf`);
    },
  },
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Sarabun&display=swap");

.font {
  font-family: "Sarabun", sans-serif;
}
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
