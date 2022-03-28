# Code for /obj/grid1
hou_node = hou.node("/obj/grid1")
hou_parent = hou_node.parent()
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hideLabel(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template2.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_1", "Render", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template2.setTags({"spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0", "Shading", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("A list of tags which can be used to select the object")
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be reflected on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be refracted on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Lights that illuminate this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_1", "Sampling", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template3.setTags({"spare_category": "Sampling"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_2", "Dicing", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_3", "Geometry", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_2", "Misc", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, file_type=hou.fileType.Any, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"filechooser_mode": "read"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/grid1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/grid1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/grid1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.setAutoscope((True, True, True))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/grid1/grid1
hou_node = hou_parent.createNode("grid", "grid1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 10.7011))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/grid1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/grid1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1000, 1000))


# Code for /obj/grid1/grid1/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/grid1")
hou_parm = hou_node.parm("rows")
hou_parm.deleteAllKeyframes()
hou_parm.set(50)


# Code for /obj/grid1/grid1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/grid1")
hou_parm = hou_node.parm("cols")
hou_parm.deleteAllKeyframes()
hou_parm.set(50)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polyextrude1
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 9.57163))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("193-195 241-244 290-293 339-342 388-391 437-440 484-489 533-538 582-587 631-636 676-685 725-734 774-783 823-832 872-881 921-930 970-979 1020-1028 1069-1077 1118-1126 1167-1175 1216-1224 1265-1273 1314-1322 1363-1371 1412-1420 1461-1469 1511-1518 1560-1567 1609-1616 1658-1665 1707-1714 1756-1763 1805-1812 1857-1861 1906-1910 1955-1959 2004-2008 2053-2057 2105-2106 2153-2155 2202-2204 2253")


# Code for /obj/grid1/polyextrude1/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(-380.98068237304688)


# Code for /obj/grid1/polyextrude1/divs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("divs")
hou_parm.deleteAllKeyframes()
hou_parm.set(4)


# Code for /obj/grid1/polyextrude1/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude1/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude1/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude1/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude1/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude1/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude1/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude1/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude1/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude1/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude1")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/blast1
hou_node = hou_parent.createNode("blast", "blast1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 8.31272))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/blast1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast1")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("2404-2446 2512-2554 2620-2662 2728-2770")


# Code for /obj/grid1/blast1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast1")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("prims")


# Code for /obj/grid1/blast1/removegrp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast1")
hou_parm = hou_node.parm("removegrp")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "generic_delete")
hou_node.setUserData("___Version___", "19.0.455")
hou_node.setUserData("___toolcount___", "2")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/mountain1
hou_node = hou_parent.createNode("attribnoise::2.0", "mountain1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 7.30087))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/mountain1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("0-42 46-48 50-92 96-98 100-142 150-192 200-225 227-230 234-242 247-272 287-289 293-318 339-364 385-410 431-456 477-502 521-546 565-590 609-634 653-678 693-712 714-718 733-752 773-793 813-833 853-873 893-913 934-954 975-995 1016-1036 1057-1077 1098-1118 1139-1159 1180-1200 1221-1241 1262-1282 1303-1323 1345-1365 1387-1407 1429-1449 1471-1491 1494-1496 1513-1538 1555-1580 1597-1622 1627-1628 1642-1667 1669-1673 1687-1712 1714-1718 1732-1757 1759-1763 1777-1802 1804-1808 1822-1847 1849-1856 1870-1904 1912 1918-1952 1955-1960 1965-2007 2014-2056 2064-2106 2110-2112 2114-2213")


# Code for /obj/grid1/mountain1/attribs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("attribs")
hou_parm.deleteAllKeyframes()
hou_parm.set("P")


# Code for /obj/grid1/mountain1/displace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("displace")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/amplitude parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("amplitude")
hou_parm.deleteAllKeyframes()
hou_parm.set(400)


# Code for /obj/grid1/mountain1/enableremap parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("enableremap")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/remapramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp")
hou_parm.deleteAllKeyframes()
hou_parm.set(3)


# Code for /obj/grid1/mountain1/elementsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("elementsize")
hou_parm.deleteAllKeyframes()
hou_parm.set(800)


# Code for /obj/grid1/mountain1/offset parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("offset")
hou_parm.deleteAllKeyframes()
hou_parm.set(28.800000000000001)


# Code for /obj/grid1/mountain1/folder6 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("folder6")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/folder4 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("folder4")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/fractal parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("fractal")
hou_parm.deleteAllKeyframes()
hou_parm.set("hmfT")


# Code for /obj/grid1/mountain1/oct parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("oct")
hou_parm.deleteAllKeyframes()
hou_parm.set(8)


# Code for /obj/grid1/mountain1/rough parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("rough")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.40000000000000002)


# Code for /obj/grid1/mountain1/folder2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("folder2")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/remapramp1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp1pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.41952788829803467)


# Code for /obj/grid1/mountain1/remapramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.76287555694580078)


# Code for /obj/grid1/mountain1/remapramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.47540983557701111)


# Code for /obj/grid1/mountain1/remapramp3pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp3pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/mountain1/remapramp3value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/mountain1")
hou_parm = hou_node.parm("remapramp3value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "geometry_mountain")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("___toolcount___", "3")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/grid1/polyextrude2
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 6.40667))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude2/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("575-576 618-619 657-658 852-853 891-892 931-932 1131-1132 1171-1172 1211-1212 1414-1415 1455-1456 1496-1497")


# Code for /obj/grid1/polyextrude2/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(115.19532012939453)


# Code for /obj/grid1/polyextrude2/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude2/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude2/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude2/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude2/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude2/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude2/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude2/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude2/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude2/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude2")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polyextrude3
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-4.4917, 5.51247))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude3/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("576-582 617-623 654-660 847-853 884-890 922-928 1120-1127 1158-1165 1196-1203 1397-1399 1436-1438 1475-1477")


# Code for /obj/grid1/polyextrude3/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(19.667102813720703)


# Code for /obj/grid1/polyextrude3/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude3/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude3/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude3/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude3/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude3/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude3/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude3/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude3/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude3/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude3")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/merge1
hou_node = hou_parent.createNode("merge", "merge1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.07079, 4.03993))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/tube1
hou_node = hou_parent.createNode("tube", "tube1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.06964, 7.40659))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/tube1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube1")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")


# Code for /obj/grid1/tube1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube1")
hou_parm = hou_node.parm("orient")
hou_parm.deleteAllKeyframes()
hou_parm.set("x")


# Code for /obj/grid1/tube1/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube1")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((6, 6))


# Code for /obj/grid1/tube1/height parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube1")
hou_parm = hou_node.parm("height")
hou_parm.deleteAllKeyframes()
hou_parm.set(100)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform1
hou_node = hou_parent.createNode("xform", "transform1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.06964, 6.45364))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((159.43642616271973, 9.4653358459472656, 225.41490364074707))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/copy1
hou_node = hou_parent.createNode("copyxform", "copy1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.06964, 5.51247))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/copy1/ncy parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy1")
hou_parm = hou_node.parm("ncy")
hou_parm.deleteAllKeyframes()
hou_parm.set(4)


# Code for /obj/grid1/copy1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, -14))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/copy2
hou_node = hou_parent.createNode("copyxform", "copy2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.19047, 6.53713))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/copy2/ncy parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy2")
hou_parm = hou_node.parm("ncy")
hou_parm.deleteAllKeyframes()
hou_parm.set(4)


# Code for /obj/grid1/copy2/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy2")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, -14))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform2
hou_node = hou_parent.createNode("xform", "transform2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.18274, 9.24511))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform2/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform2")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((223.3526554107666, 9.4653358459472656, 81.356912612915039))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/tube2
hou_node = hou_parent.createNode("tube", "tube2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.18274, 10.1981))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/tube2/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube2")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")


# Code for /obj/grid1/tube2/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube2")
hou_parm = hou_node.parm("orient")
hou_parm.deleteAllKeyframes()
hou_parm.set("x")


# Code for /obj/grid1/tube2/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube2")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((6, 6))


# Code for /obj/grid1/tube2/height parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/tube2")
hou_parm = hou_node.parm("height")
hou_parm.deleteAllKeyframes()
hou_parm.set(250)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/copy3
hou_node = hou_parent.createNode("copyxform", "copy3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.19047, 5.51247))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/copy3/ncy parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy3")
hou_parm = hou_node.parm("ncy")
hou_parm.deleteAllKeyframes()
hou_parm.set(3)


# Code for /obj/grid1/copy3/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/copy3")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, -142))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform3
hou_node = hou_parent.createNode("xform", "transform3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.72432, 8.35673))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform3/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform3")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((335.09628677368164, 112.36490249633789, 0))


# Code for /obj/grid1/transform3/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform3")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, -90))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/merge2
hou_node = hou_parent.createNode("merge", "merge2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.18932, 7.4928))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/blast2
hou_node = hou_parent.createNode("blast", "blast2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.06964, 2.66436))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/blast2/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast2")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("2835-2846 2859-2870 2883-2894 2907-2918")


# Code for /obj/grid1/blast2/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast2")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("prims")


# Code for /obj/grid1/blast2/removegrp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/blast2")
hou_parm = hou_node.parm("removegrp")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "generic_delete")
hou_node.setUserData("___Version___", "19.0.455")
hou_node.setUserData("___toolcount___", "6")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/edit1
hou_node = hou_parent.createNode("edit", "edit1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.06964, 1.77016))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/edit1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/edit1")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("2672-2675 2680-2683 2688-2691")


# Code for /obj/grid1/edit1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/edit1")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("prims")


# Code for /obj/grid1/edit1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/edit1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, -13.604167938232422, 0))


# Code for /obj/grid1/edit1/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/edit1")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((255.10202026367188, 19.667102813720703, 61.2244873046875))


# Code for /obj/grid1/edit1/leadislandhint parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/edit1")
hou_parm = hou_node.parm("leadislandhint")
hou_parm.deleteAllKeyframes()
hou_parm.set("2682")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/box1
hou_node = hou_parent.createNode("box", "box1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-8.30133, 2.07566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/box1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box1")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/grid1/box1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((60.700000000000003, 121, 100))


# Code for /obj/grid1/box1/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box1")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/merge3
hou_node = hou_parent.createNode("merge", "merge3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.65957, -7.89169))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform4
hou_node = hou_parent.createNode("xform", "transform4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-8.30133, 1.31566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform4/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform4")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((92.115993499755859, 58.824935913085938, 56.311542510986328))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/bound1
hou_node = hou_parent.createNode("bound", "bound1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-8.30133, 0.502855))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/bound1/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound1")
hou_parm = hou_node.parm("dodivs")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/bound1/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound1")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((8, 11, 10))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/bound2
hou_node = hou_parent.createNode("bound", "bound2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-6.17013, 0.502855))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/bound2/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound2")
hou_parm = hou_node.parm("dodivs")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/bound2/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound2")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((8, 11, 10))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform5
hou_node = hou_parent.createNode("xform", "transform5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-6.17013, 1.31566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform5/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform5")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((252.48447799682617, 58.824935913085938, 56.311542510986328))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/box2
hou_node = hou_parent.createNode("box", "box2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-6.17013, 2.07566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/box2/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box2")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/grid1/box2/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box2")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((174.24290084838867, 27.417694091796875, 100))


# Code for /obj/grid1/box2/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box2")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((7.6534442901611328, -46.791152954101562, 0))


# Code for /obj/grid1/box2/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box2")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/bound3
hou_node = hou_parent.createNode("bound", "bound3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.035, 0.502855))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/bound3/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound3")
hou_parm = hou_node.parm("dodivs")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/bound3/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound3")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((8, 11, 10))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform6
hou_node = hou_parent.createNode("xform", "transform6", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.035, 1.31566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform6/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform6")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((92.115993499755859, 58.824935913085938, 198.93928146362305))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/box3
hou_node = hou_parent.createNode("box", "box3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.035, 2.07566))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/box3/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box3")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/grid1/box3/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box3")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((167.83417701721191, 40.406349182128906, 100))


# Code for /obj/grid1/box3/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box3")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((53.56708812713623, -40.296825408935547, 0))


# Code for /obj/grid1/box3/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box3")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/bound4
hou_node = hou_parent.createNode("bound", "bound4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.32202, -0.0908987))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/bound4/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound4")
hou_parm = hou_node.parm("dodivs")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/bound4/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/bound4")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((8, 11, 10))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform7
hou_node = hou_parent.createNode("xform", "transform7", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.32202, 0.721901))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform7/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform7")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((382.27402877807617, -78.555267333984375, 57.187503814697266))


# Code for /obj/grid1/transform7/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform7")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, -90))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/box4
hou_node = hou_parent.createNode("box", "box4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.32202, 1.4819))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/box4/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box4")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/grid1/box4/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box4")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((174.24290084838867, 27.417694091796875, 100))


# Code for /obj/grid1/box4/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box4")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((7.6534442901611328, -46.791152954101562, 0))


# Code for /obj/grid1/box4/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box4")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/box5
hou_node = hou_parent.createNode("box", "box5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2912, 0.0698124))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/box5/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box5")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/grid1/box5/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box5")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 12.146723747253418, 1))


# Code for /obj/grid1/box5/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box5")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 5.573361873626709, 0))


# Code for /obj/grid1/box5/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/box5")
hou_parm_tuple = hou_node.parmTuple("divrate")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 2))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polyextrude4
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude4", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2912, -0.824392))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude4/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("2")


# Code for /obj/grid1/polyextrude4/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(1.6808929443359375)


# Code for /obj/grid1/polyextrude4/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude4/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude4/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude4/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude4/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude4/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude4/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude4/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude4/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude4/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude4")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polyextrude5
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2912, -1.71859))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude5/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("7")


# Code for /obj/grid1/polyextrude5/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(11.1996089220047)


# Code for /obj/grid1/polyextrude5/inset parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("inset")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.33400000000000002)


# Code for /obj/grid1/polyextrude5/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude5/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude5/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude5/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude5/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude5/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude5/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude5/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude5/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude5/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude5")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polyextrude6
hou_node = hou_parent.createNode("polyextrude::2.0", "polyextrude6", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2912, -2.61279))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polyextrude6/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("8")


# Code for /obj/grid1/polyextrude6/dist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("dist")
hou_parm.deleteAllKeyframes()
hou_parm.set(2.5108861923217773)


# Code for /obj/grid1/polyextrude6/inset parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("inset")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.28399999999999997)


# Code for /obj/grid1/polyextrude6/thicknessramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("thicknessramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude6/thicknessramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("thicknessramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude6/thicknessramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("thicknessramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude6/thicknessramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("thicknessramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude6/thicknessramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("thicknessramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude6/twistramp1value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("twistramp1value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude6/twistramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("twistramp1interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


# Code for /obj/grid1/polyextrude6/twistramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("twistramp2pos")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/grid1/polyextrude6/twistramp2value parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("twistramp2value")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)


# Code for /obj/grid1/polyextrude6/twistramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polyextrude6")
hou_parm = hou_node.parm("twistramp2interp")
hou_parm.deleteAllKeyframes()
hou_parm.set("catmull-rom")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform8
hou_node = hou_parent.createNode("xform", "transform8", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-21.2912, -3.80234))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform8/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform8")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 234.0345516204834))


# Code for /obj/grid1/transform8/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform8")
hou_parm = hou_node.parm("scale")
hou_parm.deleteAllKeyframes()
hou_parm.set(5.0099999999999998)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform9
hou_node = hou_parent.createNode("xform", "transform9", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-18.0149, -3.80234))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform9/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform9")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((100.62657833099365, 0, 142.61710166931152))


# Code for /obj/grid1/transform9/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform9")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, -39.206699999999998, 0))


# Code for /obj/grid1/transform9/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform9")
hou_parm = hou_node.parm("scale")
hou_parm.deleteAllKeyframes()
hou_parm.set(7.0499999999999998)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform10
hou_node = hou_parent.createNode("xform", "transform10", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-15.181, -3.80234))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform10/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform10")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((321.594069480896, 0, 120.57526206970215))


# Code for /obj/grid1/transform10/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform10")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 52.791600000000003, 0))


# Code for /obj/grid1/transform10/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform10")
hou_parm = hou_node.parm("scale")
hou_parm.deleteAllKeyframes()
hou_parm.set(3.8799999999999999)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/transform11
hou_node = hou_parent.createNode("xform", "transform11", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-12.7273, -3.80234))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/transform11/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform11")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((307.20078945159912, 0, -36.410196304321289))


# Code for /obj/grid1/transform11/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform11")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, -49.000218893225835, 0))


# Code for /obj/grid1/transform11/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/transform11")
hou_parm = hou_node.parm("scale")
hou_parm.deleteAllKeyframes()
hou_parm.set(4.8799999999999999)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polywire1
hou_node = hou_parent.createNode("polywire", "polywire1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-11.035, -0.843247))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polywire1/div parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire1")
hou_parm = hou_node.parm("div")
hou_parm.deleteAllKeyframes()
hou_parm.set(8)


# Code for /obj/grid1/polywire1/segscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire1")
hou_parm_tuple = hou_node.parmTuple("segscale")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polywire2
hou_node = hou_parent.createNode("polywire", "polywire2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-8.06874, -1.0869))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polywire2/div parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire2")
hou_parm = hou_node.parm("div")
hou_parm.deleteAllKeyframes()
hou_parm.set(8)


# Code for /obj/grid1/polywire2/segscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire2")
hou_parm_tuple = hou_node.parmTuple("segscale")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polywire3
hou_node = hou_parent.createNode("polywire", "polywire3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-5.99353, -1.32772))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polywire3/div parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire3")
hou_parm = hou_node.parm("div")
hou_parm.deleteAllKeyframes()
hou_parm.set(8)


# Code for /obj/grid1/polywire3/segscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire3")
hou_parm_tuple = hou_node.parmTuple("segscale")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/polywire5
hou_node = hou_parent.createNode("polywire", "polywire5", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.09316, -1.58861))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/grid1/polywire5/div parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire5")
hou_parm = hou_node.parm("div")
hou_parm.deleteAllKeyframes()
hou_parm.set(8)


# Code for /obj/grid1/polywire5/segscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/polywire5")
hou_parm_tuple = hou_node.parmTuple("segscale")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("1.0 - 1.0 / $NSEG", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/grid1/rop_fbx1
hou_node = hou_parent.createNode("rop_fbx", "rop_fbx1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-2.65842, -9.10027))
hou_node.bypass(False)
hou_node.hide(False)
hou_node.setLocked(False)
hou_node.setSelected(False)

# Code for /obj/grid1/rop_fbx1/f parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/rop_fbx1")
hou_parm_tuple = hou_node.parmTuple("f")

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FSTART", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FSTART", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FSTART", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FEND", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FEND", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("$FEND", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


# Code for /obj/grid1/rop_fbx1/sopoutput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/rop_fbx1")
hou_parm = hou_node.parm("sopoutput")
hou_parm.deleteAllKeyframes()
hou_parm.set("$HIP/layout.fbx")


# Code for /obj/grid1/rop_fbx1/convertunits parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/grid1/rop_fbx1")
hou_parm = hou_node.parm("convertunits")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/grid1/polyextrude1
hou_node = hou_parent.node("polyextrude1")
if hou_parent.node("grid1") is not None:
    hou_node.setInput(0, hou_parent.node("grid1"), 0)
# Code to establish connections for /obj/grid1/blast1
hou_node = hou_parent.node("blast1")
if hou_parent.node("polyextrude1") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude1"), 0)
# Code to establish connections for /obj/grid1/mountain1
hou_node = hou_parent.node("mountain1")
if hou_parent.node("blast1") is not None:
    hou_node.setInput(0, hou_parent.node("blast1"), 0)
# Code to establish connections for /obj/grid1/polyextrude2
hou_node = hou_parent.node("polyextrude2")
if hou_parent.node("mountain1") is not None:
    hou_node.setInput(0, hou_parent.node("mountain1"), 0)
# Code to establish connections for /obj/grid1/polyextrude3
hou_node = hou_parent.node("polyextrude3")
if hou_parent.node("polyextrude2") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude2"), 0)
# Code to establish connections for /obj/grid1/merge1
hou_node = hou_parent.node("merge1")
if hou_parent.node("polyextrude3") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude3"), 0)
if hou_parent.node("copy1") is not None:
    hou_node.setInput(1, hou_parent.node("copy1"), 0)
if hou_parent.node("copy3") is not None:
    hou_node.setInput(2, hou_parent.node("copy3"), 0)
# Code to establish connections for /obj/grid1/transform1
hou_node = hou_parent.node("transform1")
if hou_parent.node("tube1") is not None:
    hou_node.setInput(0, hou_parent.node("tube1"), 0)
# Code to establish connections for /obj/grid1/copy1
hou_node = hou_parent.node("copy1")
if hou_parent.node("transform1") is not None:
    hou_node.setInput(0, hou_parent.node("transform1"), 0)
# Code to establish connections for /obj/grid1/copy2
hou_node = hou_parent.node("copy2")
if hou_parent.node("merge2") is not None:
    hou_node.setInput(0, hou_parent.node("merge2"), 0)
# Code to establish connections for /obj/grid1/transform2
hou_node = hou_parent.node("transform2")
if hou_parent.node("tube2") is not None:
    hou_node.setInput(0, hou_parent.node("tube2"), 0)
# Code to establish connections for /obj/grid1/copy3
hou_node = hou_parent.node("copy3")
if hou_parent.node("copy2") is not None:
    hou_node.setInput(0, hou_parent.node("copy2"), 0)
# Code to establish connections for /obj/grid1/transform3
hou_node = hou_parent.node("transform3")
if hou_parent.node("transform2") is not None:
    hou_node.setInput(0, hou_parent.node("transform2"), 0)
# Code to establish connections for /obj/grid1/merge2
hou_node = hou_parent.node("merge2")
if hou_parent.node("transform2") is not None:
    hou_node.setInput(0, hou_parent.node("transform2"), 0)
if hou_parent.node("transform3") is not None:
    hou_node.setInput(1, hou_parent.node("transform3"), 0)
# Code to establish connections for /obj/grid1/blast2
hou_node = hou_parent.node("blast2")
if hou_parent.node("merge1") is not None:
    hou_node.setInput(0, hou_parent.node("merge1"), 0)
# Code to establish connections for /obj/grid1/edit1
hou_node = hou_parent.node("edit1")
if hou_parent.node("blast2") is not None:
    hou_node.setInput(0, hou_parent.node("blast2"), 0)
# Code to establish connections for /obj/grid1/merge3
hou_node = hou_parent.node("merge3")
if hou_parent.node("polywire2") is not None:
    hou_node.setInput(0, hou_parent.node("polywire2"), 0)
if hou_parent.node("edit1") is not None:
    hou_node.setInput(1, hou_parent.node("edit1"), 0)
if hou_parent.node("polywire3") is not None:
    hou_node.setInput(2, hou_parent.node("polywire3"), 0)
if hou_parent.node("polywire1") is not None:
    hou_node.setInput(3, hou_parent.node("polywire1"), 0)
if hou_parent.node("polywire5") is not None:
    hou_node.setInput(4, hou_parent.node("polywire5"), 0)
if hou_parent.node("transform8") is not None:
    hou_node.setInput(5, hou_parent.node("transform8"), 0)
if hou_parent.node("transform9") is not None:
    hou_node.setInput(6, hou_parent.node("transform9"), 0)
if hou_parent.node("transform10") is not None:
    hou_node.setInput(7, hou_parent.node("transform10"), 0)
if hou_parent.node("transform11") is not None:
    hou_node.setInput(8, hou_parent.node("transform11"), 0)
# Code to establish connections for /obj/grid1/transform4
hou_node = hou_parent.node("transform4")
if hou_parent.node("box1") is not None:
    hou_node.setInput(0, hou_parent.node("box1"), 0)
# Code to establish connections for /obj/grid1/bound1
hou_node = hou_parent.node("bound1")
if hou_parent.node("transform4") is not None:
    hou_node.setInput(0, hou_parent.node("transform4"), 0)
# Code to establish connections for /obj/grid1/bound2
hou_node = hou_parent.node("bound2")
if hou_parent.node("transform5") is not None:
    hou_node.setInput(0, hou_parent.node("transform5"), 0)
# Code to establish connections for /obj/grid1/transform5
hou_node = hou_parent.node("transform5")
if hou_parent.node("box2") is not None:
    hou_node.setInput(0, hou_parent.node("box2"), 0)
# Code to establish connections for /obj/grid1/bound3
hou_node = hou_parent.node("bound3")
if hou_parent.node("transform6") is not None:
    hou_node.setInput(0, hou_parent.node("transform6"), 0)
# Code to establish connections for /obj/grid1/transform6
hou_node = hou_parent.node("transform6")
if hou_parent.node("box3") is not None:
    hou_node.setInput(0, hou_parent.node("box3"), 0)
# Code to establish connections for /obj/grid1/bound4
hou_node = hou_parent.node("bound4")
if hou_parent.node("transform7") is not None:
    hou_node.setInput(0, hou_parent.node("transform7"), 0)
# Code to establish connections for /obj/grid1/transform7
hou_node = hou_parent.node("transform7")
if hou_parent.node("box4") is not None:
    hou_node.setInput(0, hou_parent.node("box4"), 0)
# Code to establish connections for /obj/grid1/polyextrude4
hou_node = hou_parent.node("polyextrude4")
if hou_parent.node("box5") is not None:
    hou_node.setInput(0, hou_parent.node("box5"), 0)
# Code to establish connections for /obj/grid1/polyextrude5
hou_node = hou_parent.node("polyextrude5")
if hou_parent.node("polyextrude4") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude4"), 0)
# Code to establish connections for /obj/grid1/polyextrude6
hou_node = hou_parent.node("polyextrude6")
if hou_parent.node("polyextrude5") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude5"), 0)
# Code to establish connections for /obj/grid1/transform8
hou_node = hou_parent.node("transform8")
if hou_parent.node("polyextrude6") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude6"), 0)
# Code to establish connections for /obj/grid1/transform9
hou_node = hou_parent.node("transform9")
if hou_parent.node("polyextrude6") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude6"), 0)
# Code to establish connections for /obj/grid1/transform10
hou_node = hou_parent.node("transform10")
if hou_parent.node("polyextrude6") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude6"), 0)
# Code to establish connections for /obj/grid1/transform11
hou_node = hou_parent.node("transform11")
if hou_parent.node("polyextrude6") is not None:
    hou_node.setInput(0, hou_parent.node("polyextrude6"), 0)
# Code to establish connections for /obj/grid1/polywire1
hou_node = hou_parent.node("polywire1")
if hou_parent.node("bound3") is not None:
    hou_node.setInput(0, hou_parent.node("bound3"), 0)
# Code to establish connections for /obj/grid1/polywire2
hou_node = hou_parent.node("polywire2")
if hou_parent.node("bound1") is not None:
    hou_node.setInput(0, hou_parent.node("bound1"), 0)
# Code to establish connections for /obj/grid1/polywire3
hou_node = hou_parent.node("polywire3")
if hou_parent.node("bound2") is not None:
    hou_node.setInput(0, hou_parent.node("bound2"), 0)
# Code to establish connections for /obj/grid1/polywire5
hou_node = hou_parent.node("polywire5")
if hou_parent.node("bound4") is not None:
    hou_node.setInput(0, hou_parent.node("bound4"), 0)
# Code to establish connections for /obj/grid1/rop_fbx1
hou_node = hou_parent.node("rop_fbx1")
if hou_parent.node("merge3") is not None:
    hou_node.setInput(0, hou_parent.node("merge3"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

