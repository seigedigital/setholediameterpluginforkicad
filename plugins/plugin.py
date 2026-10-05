import pcbnew
import wx
import os

def set_hole_diameter(pcb, diameter):
    new_size = pcbnew.VECTOR2I_MM(diameter, diameter)
    changed = 0
    skipped_slots = 0
    for footprint in pcb.GetFootprints():
        for pad in footprint.Pads():
            # Only plated through-hole pads are affected:
            #  - SMD / CONN pads have no drill: setting one adds a hole.
            #  - NPTH pads are mechanical/mounting holes: must keep their size.
            if pad.GetAttribute() != pcbnew.PAD_ATTRIB_PTH:
                continue
            # Leave oblong drills (slots) untouched: forcing a round size
            # would destroy the slot geometry.
            drill = pad.GetDrillSize()
            if drill.x != drill.y:
                skipped_slots += 1
                continue
            pad.SetDrillSize(new_size)
            changed += 1
            print(f"{footprint.GetReference()} pad {pad.GetPadName()}: hole set to {diameter}mm")
    print(f"{changed} PTH pad(s) updated, {skipped_slots} slotted pad(s) skipped.")

class DiameterDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(DiameterDialog, self).__init__(parent, title=title, size=(250, 150))
        self.init_ui()
        self.SetSizeHints(250, 150, 250, 150)
        self.Centre()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Hole Diameter (mm)')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(self, value="0.8")
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.on_ok)
        closeButton.Bind(wx.EVT_BUTTON, self.on_close)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_close(self, event):
        self.EndModal(wx.ID_CANCEL)

    def get_diameter(self):
        return float(self.tc.GetValue())

class SetHoleDiameterPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Set Hole Diameter"
        self.category = "Modify PCB"
        self.description = "Sets the hole diameter of all plated through-hole (PTH) pads in the PCB."
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.dark_icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        pcb = pcbnew.GetBoard()

        # Create an instance of wx.App if it doesn't already exist
        if not wx.GetApp():
            app = wx.App(False)
        else:
            app = wx.GetApp()

        dialog = DiameterDialog(None, title="Set Hole Diameter")
        if dialog.ShowModal() == wx.ID_OK:
            diameter = dialog.get_diameter()
            print(f"Setting hole diameter to {diameter}mm")
            set_hole_diameter(pcb, diameter)
            pcbnew.Refresh()
            print("Hole diameter setting completed.")
        dialog.Destroy()

SetHoleDiameterPlugin().register()
