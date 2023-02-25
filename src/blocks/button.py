from blockkit import Actions, Divider, Button


def get_back_navigate_button(offset: int):
    """Builds and returns the back navigate button"""
    return Button(text="Previous page", action_id="navigate backward", value=f"{offset}")


def get_forward_navigate_button(offset: int):
    """Builds and returns the forward navigate button"""
    return Button(text="Next page", action_id="navigate forward", value=f"{offset}")


def get_forward_and_back_navigate_button(backward_offset: int, forward_offset: int, videos_length: int) -> dict:
    """Builds and returns the front and back navigate block"""
    elements = []
    if backward_offset < 0:
        elements.append(get_forward_navigate_button(forward_offset))
        return Actions(elements=elements).build()
    if forward_offset >= videos_length:
        elements.append(get_back_navigate_button(backward_offset))
        return Actions(elements=elements).build()
    elements.append(get_back_navigate_button(backward_offset))
    elements.append(get_forward_navigate_button(forward_offset))
    return Actions(elements=elements).build()


def get_home_button() -> dict:
    """Builds and returns the home button"""
    return Actions(elements=[Button(text="Back to the home screen", value="home", action_id="home_button")]).build()


def get_divider_block() -> dict:
    """Builds and returns the divider block"""
    return Divider().build()
