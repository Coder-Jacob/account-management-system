<template>
  <div>
    <!--  add OR edit Drawer Form  -->
    <a-drawer
        :title="drawer.title"
        :width="450"
        :placement="drawer.placement"
        :visible="drawer.visible"
        :body-style="{ paddingBottom: '80px' }"
        @close="onClose"
    >
      <a-form-model layout="vertical" :model="drawer.formInline" @submit="handleSubmit" @submit.native.prevent>
        <!--    账号/密码    -->
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-model-item label="账号">
              <a-input v-model="drawer.formInline.user" placeholder="Username"/>
            </a-form-model-item>
          </a-col>
          <a-col :span="12">
            <a-form-model-item label="密码">
              <a-input v-model="drawer.formInline.password" placeholder="Password">
                <a-icon class='randomPwd' slot="prefix" type="reload" style="color:rgba(0,0,0,.25);cursor: pointer;"/>
                <!--                <a-button slot="prefix" class="Btn" shape="circle" icon="reload"/>-->
              </a-input>
            </a-form-model-item>
          </a-col>
        </a-row>
        <!--    IP/端口号    -->
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-model-item label="ip地址">
              <a-input v-model="drawer.formInline.ip" placeholder="ipAddress"/>
            </a-form-model-item>
          </a-col>
          <a-col :span="12">
            <a-form-model-item label="端口号">
              <a-input v-model="drawer.formInline.port" placeholder="端口号"/>
            </a-form-model-item>
          </a-col>
        </a-row>
        <!--    平台/企业/分类    -->
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-model-item label="平台">
              <a-input v-model="drawer.formInline.platform" placeholder="平台"/>
            </a-form-model-item>
          </a-col>
          <a-col :span="12">
            <a-form-model-item label="企业/分类">
              <a-input v-model="drawer.formInline.classify" placeholder="企业/分类"/>
            </a-form-model-item>
          </a-col>
        </a-row>
        <!--    备注    -->
        <a-row :gutter="16">
          <a-col :span="24">
            <a-form-model-item label="备注">
              <a-input v-model="drawer.formInline.remark" placeholder="备注"/>
            </a-form-model-item>
          </a-col>
        </a-row>
        <!--提交 AND 取消按钮-->
        <div
            :style="{
          position: 'absolute',
          right: 0,
          bottom: 0,
          width: '100%',
          borderTop: '1px solid #e9e9e9',
          padding: '10px 16px',
          background: '#fff',
          textAlign: 'right',
          zIndex: 1,
        }"
        >
          <a-button :style="{ marginRight: '8px' }" @click="onClose">
            取消
          </a-button>
          <a-button
              type="primary"
              html-type="submit"
              :disabled="drawer.formInline.user === '' || drawer.formInline.password === ''"
          >
            提交
          </a-button>
        </div>
      </a-form-model>
    </a-drawer>
    <!-- 列表上方操作栏 -->
    <div class="caozuo">
      <div class="left">
        <a-button class="Btn" type="primary" @click="showDrawer">新增</a-button>
        <a-button class="Btn" type="danger" @click="showDrawer">删除</a-button>
      </div>
      <div class="right">
        <a-pagination
            show-quick-jumper
            :default-current="2"
            :total="500"
            disabled
            show-less-items
            @change="onChange"
            size="small"
        />
      </div>
    </div>
    <!--  列表  -->
    <a-table
        class="accountList"
        :columns="columns"
        :data-source="data"
        :scroll="{ x: 1000 }"
        bordered
        :loading="false"
        :pagination="false"
    >
      <!--       :pagination="{disabled:false,current:2,size:'small',position:'top'}" -->
      <span slot="usernameTitle"><a-icon type="smile-o"/> 账号</span>
      <!-- 敏感字段以*号显示 -->
      <template slot="username" slot-scope="uname">
        <b class="secret">******</b>
        <a-icon
            class="copyIcon"
            type="copy"
            @click="copytxt(uname, 0, '用户名')"
        />
      </template>
      <template slot="pwd" slot-scope="passwd">
        <b>******</b>
        <a-icon
            class="copyIcon"
            type="copy"
            @click="copytxt(passwd, 0, '密码')"
        />
      </template>
      <template slot="ip" slot-scope="ipAdress">
        <b>******</b>
        <a-icon
            class="copyIcon"
            type="copy"
            @click="copytxt(ipAdress, 0, 'ip地址')"
        />
      </template>
      <template slot="port" slot-scope="ports">
        <b>******</b>
        <a-icon
            class="copyIcon"
            type="copy"
            @click="copytxt(ports, 0, '端口号')"
        />
      </template>

      <template slot="operation" slot-scope="data">
        <div class="operation">
          <!-- 实线Icon -->
          <a-icon type="edit" theme="filled"/>
          <a-icon type="eye" theme="filled"/>
          <a-icon
              type="copy"
              theme="filled"
              @click="copytxt(data, 1, '账号信息')"
          />
          <a-icon type="delete" theme="filled"/>
        </div>
      </template>
    </a-table>
  </div>
</template>
<script>
const columns = [
  {
    dataIndex: "username",
    rowKey: "1",
    width: 105,
    align: "center",
    slots: {title: "usernameTitle"},
    scopedSlots: {customRender: "username"},
    filters: [
      {
        text: "Joe",
        value: "spider1",
      },
      {
        text: "Jim",
        value: "Jim",
      },
    ],
  },
  {
    title: "密码",
    dataIndex: "pwd",
    key: "2",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "pwd"},
  },
  {
    title: "IP",
    dataIndex: "ip",
    key: "3",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "ip"},
  },
  {
    title: "端口号",
    dataIndex: "port",
    key: "4",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "port"},
  },
  {
    title: "平台",
    dataIndex: "platform",
    key: "5",
    width: 150,
    align: "center",
    filters: [
      {
        text: "Joe",
        value: "spider1",
      },
      {
        text: "Jim",
        value: "Jim",
      },
    ],
  },
  {
    title: "企业/分类",
    dataIndex: "classify",
    key: "6",
    width: 130,
    align: "center",
    filters: [
      {
        text: "Joe",
        value: "spider1",
      },
      {
        text: "Jim",
        value: "Jim",
      },
    ],
  },
  {title: "备注", dataIndex: "remark", key: "7", width: 170, align: "center"},
  {
    title: "操作",
    key: "operation",
    width: 200,
    scopedSlots: {customRender: "operation"},
    align: "center",
  },
];
const data = [];
for (let i = 0; i < 8; i++) {
  data.push({
    username: `spider${i + 1}`,
    pwd: `password ${i + 1}`,
    ip: `192.168.1.${i + 1}`,
    port: `808${i}`,
    platform: `服务器${i + 1}`,
    classify: `单位${i + 1}`,
    remark: `练习服务器${i + 1}`,
    id: i,
  });
}
const pageSizeOptions = ["5", "10", "20", String(data.length)];

import {mapState} from "vuex";
import ClipboardJS from "clipboard";

export default {
  name: "serviceAccount",
  i18n: require("./i18n"),
  data() {
    return {
      data,
      columns,
      pageSizeOptions,
      // add OR edit DrawerForm Settings
      drawer: {
        title: '新增数据',
        visible: false,
        placement: 'right',
        formInline: {
          user: '',
          password: '',
          ip: '',
          port: '',
          platform: '',
          classify: '',
          remark: '',
          id: '',
        },
      }
    };
  },
  computed: {
    ...mapState("setting", ["pageMinHeight"]),
    desc() {
      return this.$t("description");
    },
  },
  mounted() {
    this.testPost();
  },
  methods: {
    // 异步请求获取数据接口
    async testPost() {
      this.axios({
        url: "account/getac",
        mothod: "get",
      }).then(res => {
        console.log(res);
      }).catch(error => {
        console.log(error);
      })
    },
    // 复制账号信息
    copytxt(txt, operate, msg) {
      if (operate === 1) {
        var content =
            txt.classify +
            "-" +
            txt.platform +
            "\n" +
            "ip地址：" +
            txt.ip +
            ":" +
            txt.port +
            "\n" +
            "账号：" +
            txt.username +
            "\n" +
            "密码：" +
            txt.pwd; // 将想要复制的值
      } else {
        content = txt;
      }
      var clipboard = new ClipboardJS(".accountList", {
        text: function (trigger) {
          return content;
        },
      });

      clipboard.on("success", () => {
        this.$message.success(msg + "复制成功！");
        clipboard.destroy();
      });
      clipboard.on("error", () => {
        this.$message.error(msg + "复制失败！");
        clipboard.destroy();
      });
    },
    // 显示新增表单抽屉
    showDrawer() {
      this.drawer.visible = true;
    },
    // 关闭新增表单抽屉
    onClose() {
      this.drawer.visible = false;
    },
    // 提交表单
    handleSubmit() {
      alert('提交成功')
      console.log(this.drawer.formInline)
      // this.drawer.visible = false;
    }
  },
};
</script>

<style scoped lang="less">
  @import "index";
</style>