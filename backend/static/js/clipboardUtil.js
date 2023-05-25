// import {ELEMENT} from "../lib-master";

function copyWithElement(item, str) {
    console.log('this is clicked item:', item);
    copyStr(str)
    $(item).popover({content:"fuck you!"})
}

function copyFromElementAttr(item, attr) {
    console.log('this is clicked item:', item);
    copyStr(item.getAttribute(attr))
    $(item).modal()``
}

// 复制单文本（密码，账号等）
function copyStr(str) {
    var clipboard = new ClipboardJS('body',{
        text: function (trigger){
            return str
        }
    });
    // 复制成功
    clipboard.on("success", ()=>{
        showModal('success', '复制成功')
        clipboard.destroy()
    })
    // 复制失败
    clipboard.on("error", () => {
        showModal('error', '复制失败')
    })
}

// 复制账号所有信息，按照文本样式
function copyText(content){
    content = content.replaceAll('/jcb/','\n')
    var clipboard = new ClipboardJS("body", {
        text: function (trigger) {
            return content;
        },
    });

    // 复制成功
    clipboard.on("success", () => {
        showModal('success', '账号信息复制成功')
        clipboard.destroy();
    });
    // 复制失败
    clipboard.on("error", () => {
        showModal('error', '账号信息复制失败')
        clipboard.destroy();
    });
}

// 显示Element Message 提示信息
function showModal(type, msg){
    // 这里的ELEMENT要大写，要不然会找不到element
    ELEMENT.Message({
        message: msg,
            type: type,
            duration: 2000
    })
}