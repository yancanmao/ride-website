# 网站验证记录 · 2026-11-05

本记录只验收展示网站，不增加 Controller、真实硬件或性能的验收范围。

## 本地检查

命令：`python3 tools/check_site.py`

```json
{
  "status": "PASS",
  "html_documents": 2,
  "local_links": 35,
  "original_figure_hashes": "2/2 match",
  "hardware": "NOT_RUN",
  "scope": "Static website checks only"
}
```

`git diff --cached --check`：通过。独立的 `node --check script.js` 因主机未提供 node 命令未运行；页面 JavaScript 在实际浏览器执行，语言切换与持久偏好已验证，浏览器捕获的 error/warn 日志为空。不用浏览器运行替代未执行的命令回执。

## 浏览器检查

在本地 HTTP 服务中实际执行：

- 首页中英文切换，标题、链接和 Controller 详情跟随切换。
- KV “当前实现与验证范围”真实展开，显示物理搬运未验收的边界。
- 从 KV 卡片进入独立详情页 `docs/controllers.html#kv`，语言偏好保留；详情页切回英文可用。
- 原图、标识与样式正常加载；页面没有第三方字体或脚本依赖。
- 窄屏实测 `innerWidth=325`、`scrollWidth=312`；桌面实测 `innerWidth=1200`、`scrollWidth=1187`，未观察到水平内容溢出（浏览器工具的视口缩放后实际 CSS 宽度，以读取值为准）。

公开部署状态以 GitHub Pages 实际构建结果和公开 HTTP 检查为准，不能用成功 push 代替部署。

## 2026-11-05 系统架构扩展

新增独立架构页与首页入口；包含系统分层和请求/控制/观测两张图。结构化IR为源，生成可编辑draw.io与SVG；drawio工具doctor通过、Desktop不可用，未宣称原生Desktop PNG导出。两页预览已在实际浏览器视觉检查，缩短了被预览器截断的说明。最终audit评分100、0错误/0警告，security通过。

网站检查当前为3个HTML、57个本地链接，两个原图SHA保持一致。新增架构页中英文、draw.io下载地址、原图入口通过本地浏览器核对。Controller新增功能以67项本地软件检查为界；真实Ray/模型/物理KV/收益未验。

## 六类型云端CPU回执更新

控制器实现/验收来源d0509be（私有仓库），代码58e9ead。六策略标准RIDE云端CPU生命周期已通过，本地与Linux各68项软件检查通过。公开固定版本摘要assets/architecture/validation-summary.json不含平台ID、地址或凭据；Ray分布式、模型/物理KV/性能维持NOT_RUN。更新只修正状态说明，不改架构IR或历史证据。
