def workshop_setup_order_solution(tools: dict[str, list[str]]) -> list[str]:
    remaining = {
        name: [dep for dep in deps if dep in tools]
        for name, deps in tools.items()
    }
    order: list[str] = []
    while remaining:
        ready = sorted(name for name, deps in remaining.items() if not deps)
        if not ready:
            return []
        order.extend(ready)
        for name in ready:
            del remaining[name]
        for deps in remaining.values():
            for name in ready:
                if name in deps:
                    deps.remove(name)
    return order
