from ._core import visual_action,parseint_from_args, dict_to_object
from xbot.app import dialog

import json
import uuid
from collections import namedtuple

# 虽然在指令树中不再透出来了，但是部分老版本的应用仍然依赖它
@visual_action
def show_alert(**args):
    """
    {
        'message': '...'
        'title': '...'
    }
    """
    dialog.show_alert(args['message'], args['title'])


# 虽然在指令树中不再透出来了，但是部分老版本的应用仍然依赖它
@visual_action
def show_confirm(**args) -> bool:
    """
    {
        'message': '...'
        'title': '...'
    }
    """
    return dialog.show_confirm(args['message'], args['title'])


@visual_action
def show_custom_dialog(**args) -> object:
    """
    {
        'settings': '...'
    }
    """

    is_auto_click = args.get('is_auto_click', False)
    timeout = parseint_from_args(args, 'timeout')
    if not is_auto_click:
        timeout = -1

    settings_str = args['settings']
    if settings_str is None or settings_str == '':
        return None
    else:
        settings = json.loads(args['settings'])
        setting_json = {
            'dialog_title':args['dialog_title'],
            'default_btn': args.get('default_btn', None),
            'timeout': timeout,
            'settings':settings
        }
        result_dict = dialog.show_custom_dialog(setting_json)
        # robot返回的result是dict，这里转换成object

        class_name = f'CustomDialogResult_Dynamic_{str(uuid.uuid1())}'
        class_name = class_name.replace('-', '_')
        return dict_to_object(class_name, result_dict)

@visual_action
def show_message_box(**args) -> str:
    """
    {
        'settings': '...'
    }
    """
    title=args['title']
    message=args['message']
    buttonstr=args['buttons']
    default_button=args['default_button']
    use_wait_timeout=args['use_wait_timeout']
    timeout = parseint_from_args(args, 'wait_seconds') if use_wait_timeout else -1
    buttonstr = _buttonstr_converter(buttonstr)
    default_button = _default_button_converter(default_button)

    result = dialog.show_message_box(title, message, buttonstr, timeout=timeout, default_button=default_button)
    return _result_converter(result)


@visual_action
def show_workbook_dialog(**args) -> str:
    """
        'title': '...'
        'message': '...'
    """
    result = dialog.show_workbook_dialog(args['title'], args['message'])
    return _result_converter(result)

@visual_action
def show_notifycation(**args):
    dialog.show_notifycation(args['message'], placement=args['placement'], level=args['level'], timeout=args['timeout'])


def _buttonstr_converter(buttonstr) -> str:
    if buttonstr == '确定':
        buttonstr = 'ok'
    elif buttonstr == '确定|取消':
        buttonstr = 'okcancel'
    elif buttonstr == '是|否':
        buttonstr = 'yesno'
    elif buttonstr == '是|否|取消':
        buttonstr = 'yesnocancel'
    else:
        buttonstr = 'ok'
    return buttonstr

def _result_converter(result) -> str:
    if result == 'ok':
         result = '确定'
    elif result == 'yes':
        result = '是'
    elif result == 'no':
        result = '否'
    elif result == 'cancel':
        result = '取消'
    else:
        result = '确定'
    return result

def _default_button_converter(default_button) -> str:
    if default_button == '确定':
        default_button = 'ok'     
    elif default_button == '是':
        default_button = 'yes' 
    elif default_button == '否':
        default_button = 'no'       
    elif default_button == '取消':
        default_button = 'cancel'
    else:
        default_button = 'ok'
    return default_button