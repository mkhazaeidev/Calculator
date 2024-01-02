def sort_menu_by_order(menu_items: dict):
    func = lambda x: x[1]['order']
    return dict(sorted(menu_items.items(), key=func))