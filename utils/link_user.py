import sql_func
import html

def link_user(id):
    return f"<a href='{sql_func.check_link(id)}'>{html.escape(sql_func.check_name(id))}</a>"