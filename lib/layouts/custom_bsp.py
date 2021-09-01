from libqtile.layout import Bsp

class BorderOnSingleBSP(Bsp):

    def configure(self, client, screen_rect):
        self.root.calc_geom(screen_rect.x, screen_rect.y, screen_rect.width,
                            screen_rect.height)
        node = self.get_node(client)
        color = self.border_focus if client.has_focus else self.border_normal
        border = self.border_width
        if node is not None:
            client.place(
                node.x,
                node.y,
                node.w - 2 * border,
                node.h - 2 * border,
                border,
                color,
                margin=self.margin)
        client.unhide()
