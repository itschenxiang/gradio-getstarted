import gradio as gr
import pandas as pd


operator_dict = {
    "产品": "documentqa@product2025",
    "测试": None,
    "研发": "documentqa@developer2025",
    "实习生": None
}

def charge(quantity, animal, countries, place, activity_list, operator, password):
    # todo
    if quantity == 'test':
        data = {
            "userId": [""], "状态": [""], "权益ID": [""], "权益开始时间": [""], "权益结束时间": [""]
        }
    else:
        data = {
            "提示": ["失败原因"]
        }
    return pd.DataFrame(data)
demo = gr.Interface(
    charge,
    [
        gr.Radio(["test", "online"], value="test", label="*环境",
                 info="不同环境会员有效期可能不同，具体可@研发"),
        gr.Radio(["周会员(不连续包周)", "年会员"], value="周会员(不连续包周)", label="*权益（套餐）类型"),
        gr.Textbox(lines=3, placeholder="多个用户换行分隔", max_lines=20, label="userId列表",
                   info="*userId列表优先(userId列表为空才会使用手机号列表)"),
        gr.Textbox(lines=3, placeholder="多个手机号换行分隔", max_lines=20, label="手机号列表"),
        gr.Dropdown(["1"], value="1", label="*数量", info="对当前批次所有用户生效(目前仅支持设置为1)"),
        gr.Dropdown(list(operator_dict.keys()), value="研发", label="*操作人类型"),
        gr.Textbox(type="password", placeholder="Token", label="Token",
                   info="test环境不用填写Token")
    ],
    gr.Dataframe(label="充值结果(服务端不保存操作记录，请检查结果后再退出或重新提交!)"),
)

if __name__ == "__main__":
    demo.launch()
