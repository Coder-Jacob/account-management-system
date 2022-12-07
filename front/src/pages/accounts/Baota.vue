<template>
  <div>
    <!--  add OR edit Drawer Form（编辑 + 新增） -->
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
        <a-button class="Btn" type="danger" disabled>删除</a-button>
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
    <!--  数据列表  -->
    <a-table
        class="accountList"
        :columns="columns"
        :data-source="data"
        :scroll="{ x: 1000 }"
        bordered
        :loading="isLoading"
        :pagination="false"
    >
      <!-- 表格头优化 -->
      <span slot="usernameTitle"><a-icon type="smile-o"/> 账号</span>
      <!-- 敏感字段数据以*号显示 -->
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
      <template slot="BasicAuthUser" slot-scope="BasicAuthUser">
        <span v-if="BasicAuthUser==='none'">{{ BasicAuthUser }}</span>
        <div v-else>
          <b>******</b>
          <a-icon
              class="copyIcon"
              type="copy"
              @click="copytxt(BasicAuthUser, 0, 'BasicAuthUser')"
          />
        </div>
      </template>
      <template slot="BasicAuthPwd" slot-scope="BasicAuthPwd">
        <span v-if="BasicAuthPwd==='none'">{{ BasicAuthPwd }}</span>
        <div v-else>
          <b>******</b>
          <a-icon
              class="copyIcon"
              type="copy"
              @click="copytxt(BasicAuthPwd, 0, 'BasicAuthPwd')"
          />
        </div>
      </template>
      <template slot="url" slot-scope="urls">
        <b>******</b>
        <a-icon
            class="copyIcon"
            type="copy"
            @click="copytxt(urls, 0, '链接')"
        />
      </template>
      <!-- 操作 -->
      <template slot="operation" slot-scope="data">
        <div class="operation">
          <!-- 查看 -->
          <a-popover title="账号详情" trigger="click">
            <template slot="content">
              <p>链接：{{ data.Links }}</p>
              <p>用户名：{{ data.userName }}</p>
              <p>密码：{{ data.Pwd }}</p>
              <p>BasicAuthUser：{{ data.BasicAuthUser }}</p>
              <p>BasicAuthPwd：{{ data.BasicAuthPwd }}</p>
            </template>
            <!--            <a-button type="primary">-->
            <a-tooltip>
              <template slot="title">
                查看账号详情
              </template>
              <a-icon type="eye" theme="filled"/>
            </a-tooltip>
            <!--            </a-button>-->
          </a-popover>
          <!-- 复制 -->
          <a-tooltip>
            <template slot="title">
              复制账号信息
            </template>
            <a-icon
                type="copy"
                theme="filled"
                @click="copytxt(data, 1, '账号信息')"
            />
          </a-tooltip>
          <!-- 修改 -->
          <a-tooltip>
            <template slot="title">
              编辑
            </template>
            <a-icon type="edit" theme="filled"/>
          </a-tooltip>
          <!-- 删除 -->
          <a-tooltip>
            <template slot="title">
              删除
            </template>
            <a-icon type="delete" theme="filled"/>
          </a-tooltip>
        </div>
      </template>
    </a-table>
  </div>
</template>
<script>
const columns = [
  {
    dataIndex: "userName",
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
    dataIndex: "Pwd",
    key: "2",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "pwd"},
  },
  {
    title: "BasicAuthUser",
    dataIndex: "BasicAuthUser",
    key: "3",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "BasicAuthUser"},
  },
  {
    title: "BasicAuthPwd",
    dataIndex: "BasicAuthPwd",
    key: "4",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "BasicAuthPwd"},
  },
  {
    title: "链接",
    dataIndex: "Links",
    key: "5",
    width: 105,
    align: "center",
    scopedSlots: {customRender: "url"},
  },
  {
    title: "平台",
    dataIndex: "Platform",
    key: "6",
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
    dataIndex: "enterprice_id",
    key: "7",
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
  {title: "备注", dataIndex: "remarks", key: "7", width: 170, align: "center"},
  {
    title: "操作",
    key: "operation",
    width: 200,
    scopedSlots: {customRender: "operation"},
    align: "center",
  },
];
const data = [];
// for (let i = 0; i < 8; i++) {
//   data.push({
//     id: i,
//     userName: `spider${i + 1}`,
//     Pwd: `password ${i + 1}`,
//     BasicAuthUser: 'BasicAuthUser',
//     BasicAuthPwd: 'BasicAuthPwd',
//     Links:'url',
//     Platform: `服务器${i + 1}`,
//     enterprice: `单位${i + 1}`,
//     remarks: `练习服务器${i + 1}`,
//   });
// }
const pageSizeOptions = ["5", "10", "20", String(data.length)];

import {mapState} from "vuex";
import ClipboardJS from "clipboard";

export default {
  name: "Demo",
  i18n: require("./i18n"),
  data() {
    return {
      data: [],
      isLoading: true,
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
          enterprice_id: '',
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
    /**
     *@desc 异步请求获取数据接口
     *@author Jacob
     *@Email jacob1109@126.com
     *@date 2022/11/29 02:02:53
     */
    async testPost() {
      this.$axios({
        url: "account/getac",
        mothod: "get",
        params: {
          'm': 2
        }
      }).then(res => {
        console.log(res);
        this.data = res.data.data
        this.isLoading = false
      }).catch(error => {
        this.$message.error("数据请求失败，请联系后端开发人员~");
        this.isLoading = false
      })
    },
    /**
     *@desc 复制账号信息
     *@author Jacob
     *@Email jacob1109@126.com
     *@date 2022/11/29 02:03:08
     */
    copytxt(txt, operate, msg) {
      if (operate === 1) {
        var content =
            txt.enterprice_id +
            "-" +
            txt.Platform +
            "\n" +
            "地址：" +
            txt.ipAddres +
            ":" +
            txt.port +
            "\n" +
            "账号：" +
            txt.userName +
            "\n" +
            "密码：" +
            txt.Pwd +
            "\n" +
            "BasicAuthUser：" +
            txt.BasicAuthUser +
            "\n" +
            "BasicAuthPwd：" +
            txt.BasicAuthPwd
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
    /**
     *@desc 显示新增表单抽屉
     *@author Jacob
     *@Email jacob1109@126.com
     *@date 2022/11/29 02:03:27
     */
    showDrawer() {
      this.drawer.visible = true;
    },
    /**
     *@desc 关闭新增表单抽屉
     *@author Jacob
     *@Email jacob1109@126.com
     *@date 2022/11/29 02:05:39
     */
    onClose() {
      this.drawer.visible = false;
    },
    /**
     *@desc提交表单
     *@author Jacob
     *@Email jacob1109@126.com
     *@date 2022/11/29 02:06:58
     */
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