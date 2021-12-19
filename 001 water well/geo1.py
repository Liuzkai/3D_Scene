# Code for /obj/geo1
hou_node = hou.node("/obj/geo1")
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
# Code for /obj/geo1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/geo1/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.setAutoscope((True, True, True))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/box1
hou_node = hou_parent.createNode("box", "box1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, 3.82313))
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

# Code for /obj/geo1/box1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/box1")
hou_parm = hou_node.parm("type")
hou_parm.deleteAllKeyframes()
hou_parm.set("polymesh")


# Code for /obj/geo1/box1/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/box1")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((2, 2, 6))


# Code for /obj/geo1/box1/divrate parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/box1")
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

# Code for /obj/geo1/bound1
hou_node = hou_parent.createNode("bound", "bound1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, 2.94824))
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

# Code for /obj/geo1/bound1/dodivs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bound1")
hou_parm = hou_node.parm("dodivs")
hou_parm.deleteAllKeyframes()
hou_parm.set(1)


# Code for /obj/geo1/bound1/divs parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/bound1")
hou_parm_tuple = hou_node.parmTuple("divs")
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 5, 10))


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/convertline1
hou_node = hou_parent.createNode("convertline", "convertline1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, 1.98918))
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

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/initial_dir
hou_node = hou_parent.createNode("attribwrangle", "initial_dir", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.80221, -2.09582))
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

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1", "Code", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("group", "Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l -a attribvop1 bindgroup", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringToggle)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_action": "import soputils\nkwargs['geometrytype'] = kwargs['node'].parmTuple('grouptype')\nkwargs['inputindex'] = 0\nsoputils.selectGroupParm(kwargs)", "script_action_help": "Select geometry from an available viewport.", "script_action_icon": "BUTTONS_reselect"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("grouptype", "Group Type", menu_items=(["guess","vertices","edges","points","prims"]), menu_labels=(["Guess from Group","Vertices","Edges","Points","Primitives"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("class", "Run Over", menu_items=(["detail","primitive","point","vertex","number"]), menu_labels=(["Detail (only once)","Primitives","Points","Vertices","Numbers"]), default_value=2, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_numcount", "Number Count", 1, default_value=([10]), min=0, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_threadjobsize", "Thread Job Size", 1, default_value=([1024]), min=1, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("snippet", "VEXpression", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="import vexpressionmenu\n\nreturn vexpressionmenu.buildSnippetMenu('attribwrangle/snippet')", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "editor": "1", "editorlang": "VEX", "editorlines": "8-30", "script_action": "import vexpressionmenu\n\nnode = kwargs['node']\nparmname = 'snippet'\n\nvexpressionmenu.createSpareParmsFromChCalls(node, parmname)", "script_action_help": "Creates spare parameters for each unique call of ch() ", "script_action_icon": "BUTTONS_create_parm_from_ch"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("exportlist", "Attributes to Create", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_strict", "Enforce Prototypes", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1_1", "Bindings", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("autobind", "Autobind by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("bindings", "Number of Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindname#", "Attribute Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("groupautobind", "Autobind Groups by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("groupbindings", "Group Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupname#", "Group Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_cwdpath", "Evaluation Node Path", 1, default_value=(["."]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_outputmask", "Export Parameters", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_updatenmls", "Update Normals If Displaced", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_matchattrib", "Attribute to Match", 1, default_value=(["id"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_inplace", "Compute Results In Place", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_selectiongroup", "Output Selection Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_precision", "VEX Precision", 1, default_value=(["auto"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["auto","32","64"]), menu_labels=(["Auto","32-bit","64-bit"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("seed", "Seed", 1, default_value=([0]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/initial_dir/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/initial_dir")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("current")


# Code for /obj/geo1/initial_dir/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/initial_dir")
hou_parm = hou_node.parm("snippet")
hou_parm.deleteAllKeyframes()
hou_parm.set("v@dir = rand(@ptnum + ch(\"seed\"));")


# Code for /obj/geo1/initial_dir/seed parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/initial_dir")
hou_parm = hou_node.parm("seed")
hou_parm.deleteAllKeyframes()
hou_parm.set(0.48899999999999999)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/group1
hou_node = hou_parent.createNode("groupcreate", "group1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, 0.98918))
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

# Code for /obj/geo1/group1/groupname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group1")
hou_parm = hou_node.parm("groupname")
hou_parm.deleteAllKeyframes()
hou_parm.set("current")


# Code for /obj/geo1/group1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group1")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("point")


# Code for /obj/geo1/group1/basegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group1")
hou_parm = hou_node.parm("basegroup")
hou_parm.deleteAllKeyframes()
hou_parm.set("6 9")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/group2
hou_node = hou_parent.createNode("groupcreate", "group2", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, -0.0408196))
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

# Code for /obj/geo1/group2/groupname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group2")
hou_parm = hou_node.parm("groupname")
hou_parm.deleteAllKeyframes()
hou_parm.set("novisit")


# Code for /obj/geo1/group2/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group2")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("point")


# Code for /obj/geo1/group2/basegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group2")
hou_parm = hou_node.parm("basegroup")
hou_parm.deleteAllKeyframes()
hou_parm.set("!0")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/group3
hou_node = hou_parent.createNode("groupcreate", "group3", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, -1.04082))
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

# Code for /obj/geo1/group3/groupname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group3")
hou_parm = hou_node.parm("groupname")
hou_parm.deleteAllKeyframes()
hou_parm.set("visited")


# Code for /obj/geo1/group3/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group3")
hou_parm = hou_node.parm("grouptype")
hou_parm.deleteAllKeyframes()
hou_parm.set("point")


# Code for /obj/geo1/group3/groupbase parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/group3")
hou_parm = hou_node.parm("groupbase")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/foreach_end1
hou_node = hou_parent.createNode("block_end", "foreach_end1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79761, -10.2392))
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

# Code for /obj/geo1/foreach_end1/itermethod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("itermethod")
hou_parm.deleteAllKeyframes()
hou_parm.set("count")


# Code for /obj/geo1/foreach_end1/iterations parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("iterations")
hou_parm.deleteAllKeyframes()
hou_parm.set(10000)


# Code for /obj/geo1/foreach_end1/maxiter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("maxiter")
hou_parm.deleteAllKeyframes()
hou_parm.set(25)


# Code for /obj/geo1/foreach_end1/blockpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("blockpath")
hou_parm.deleteAllKeyframes()
hou_parm.set("../foreach_begin1")


# Code for /obj/geo1/foreach_end1/templatepath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("templatepath")
hou_parm.deleteAllKeyframes()
hou_parm.set("../foreach_begin1")


# Code for /obj/geo1/foreach_end1/stopcondition parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_end1")
hou_parm = hou_node.parm("stopcondition")
hou_parm.deleteAllKeyframes()
hou_parm.set(0)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("detail(opinputpath(\".\",0),\"stop\",0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("detail(opinputpath(\".\",0),\"stop\",0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("detail(opinputpath(\".\",0),\"stop\",0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setFrame(1)
hou_keyframe.setExpression("detail(opinputpath(\".\",0),\"stop\",0)", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


hou_node.setColor(hou.Color([0.75, 0.4, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/foreach_begin1
hou_node = hou_parent.createNode("block_begin", "foreach_begin1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79761, -5.71722))
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

# Code for /obj/geo1/foreach_begin1/blockpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_begin1")
hou_parm = hou_node.parm("blockpath")
hou_parm.deleteAllKeyframes()
hou_parm.set("../foreach_end1")


hou_node.setColor(hou.Color([0.75, 0.4, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/foreach_count1
hou_node = hou_parent.createNode("block_begin", "foreach_count1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.61039, -5.71722))
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

# Code for /obj/geo1/foreach_count1/method parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_count1")
hou_parm = hou_node.parm("method")
hou_parm.deleteAllKeyframes()
hou_parm.set("metadata")


# Code for /obj/geo1/foreach_count1/blockpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/foreach_count1")
hou_parm = hou_node.parm("blockpath")
hou_parm.deleteAllKeyframes()
hou_parm.set("../foreach_end1")


hou_node.setColor(hou.Color([0.75, 0.4, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/compile_end1
hou_node = hou_parent.createNode("compile_end", "compile_end1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79761, -11.4722))
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

hou_node.setColor(hou.Color([0.75, 0.75, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/compile_begin1
hou_node = hou_parent.createNode("compile_begin", "compile_begin1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79761, -4.48422))
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

# Code for /obj/geo1/compile_begin1/blockpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/compile_begin1")
hou_parm = hou_node.parm("blockpath")
hou_parm.deleteAllKeyframes()
hou_parm.set("../compile_end1")


hou_node.setColor(hou.Color([0.75, 0.75, 0]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/path_iteration
hou_node = hou_parent.createNode("attribwrangle", "path_iteration", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.80221, -7.79712))
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

# Code for /obj/geo1/path_iteration/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/path_iteration")
hou_parm = hou_node.parm("group")
hou_parm.deleteAllKeyframes()
hou_parm.set("current")


# Code for /obj/geo1/path_iteration/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/path_iteration")
hou_parm = hou_node.parm("snippet")
hou_parm.deleteAllKeyframes()
hou_parm.set("int neigs[] = neighbours(0, @ptnum);\nint nextpts[] = array();\nforeach(int neig; neigs){\n    \n    if( inpointgroup(0, \"novisit\",neig)){\n        append(nextpts, neig);\n    }\n}\n\nif(len(nextpts)==0){\n    i@group_current = 0;\n    setdetailattrib(0, \"add_cur\", 1, \"add\");\n}else{\n\n    vector next_pos;\n    vector next_dir;\n    float mindot = -100;\n    float curdot;\n    int right_next;\n    vector right_dir;\n    foreach(int next; nextpts){\n        next_pos = point(0, \"P\", next);\n        next_dir = normalize(next_pos - @P);\n        curdot = dot(next_dir,v@dir);\n        if( curdot > mindot)\n        {\n            mindot = curdot;\n            right_next = next;\n            right_dir = next_dir;\n        }\n    }\n    \n    int cur_prims[] = pointprims(0, @ptnum);\n    int nex_prims[] = pointprims(0, right_next);\n    \n    foreach(int pr; cur_prims){\n        if( find(nex_prims, pr) < 0 && !inprimgroup(0, \"path\", pr)){\n            removeprim(0, pr, 0);\n        }else{\n            setprimgroup(0, \"path\", pr, 1, \"set\");\n        \n        }\n    \n    }\n    \n    i@group_current = 0;\n    i@group_novisit = 0;\n    i@group_visited = 1;\n    \n    \n    setpointgroup(0, \"current\", right_next, 1, \"set\");\n    setpointgroup(0, \"novisit\", right_next, 0, \"set\");\n    setpointattrib(0, \"dir\", right_next, right_dir, \"set\");\n\n}\n\n")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/polywire1
hou_node = hou_parent.createNode("polywire", "polywire1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.79921, -12.5847))
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

# Code for /obj/geo1/polywire1/div parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/polywire1")
hou_parm = hou_node.parm("div")
hou_parm.deleteAllKeyframes()
hou_parm.set(9)


# Code for /obj/geo1/polywire1/segscale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/polywire1")
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

# Code for /obj/geo1/initial_cur_num
hou_node = hou_parent.createNode("attribwrangle", "initial_cur_num", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.80221, -3.17362))
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

# Code for /obj/geo1/initial_cur_num/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/initial_cur_num")
hou_parm = hou_node.parm("class")
hou_parm.deleteAllKeyframes()
hou_parm.set("detail")


# Code for /obj/geo1/initial_cur_num/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/initial_cur_num")
hou_parm = hou_node.parm("snippet")
hou_parm.deleteAllKeyframes()
hou_parm.set("i@stop = 0;")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/attribcreate1
hou_node = hou_parent.createNode("attribcreate::2.0", "attribcreate1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.80266, -6.71722))
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

# Code for /obj/geo1/attribcreate1/name1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribcreate1")
hou_parm = hou_node.parm("name1")
hou_parm.deleteAllKeyframes()
hou_parm.set("add_cur")


# Code for /obj/geo1/attribcreate1/existing1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribcreate1")
hou_parm = hou_node.parm("existing1")
hou_parm.deleteAllKeyframes()
hou_parm.set("replace")


# Code for /obj/geo1/attribcreate1/class1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribcreate1")
hou_parm = hou_node.parm("class1")
hou_parm.deleteAllKeyframes()
hou_parm.set("detail")


# Code for /obj/geo1/attribcreate1/type1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/attribcreate1")
hou_parm = hou_node.parm("type1")
hou_parm.deleteAllKeyframes()
hou_parm.set("int")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.455")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.455")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/add_cur_if_lost
hou_node = hou_parent.createNode("attribwrangle", "add_cur_if_lost", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-1.80221, -8.87492))
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

# Code for /obj/geo1/add_cur_if_lost/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/add_cur_if_lost")
hou_parm = hou_node.parm("class")
hou_parm.deleteAllKeyframes()
hou_parm.set("detail")


# Code for /obj/geo1/add_cur_if_lost/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/add_cur_if_lost")
hou_parm = hou_node.parm("snippet")
hou_parm.deleteAllKeyframes()
hou_parm.set("int pts[] = expandpointgroup(0, \"novisit\");\nif( len(pts) > 0 ){\n    int iteration = detail(3, \"iteration\");\n    for(int i = 0; i < i@add_cur; i++){\n        int num = len(pts);\n        \n        int index = floor(rand(i + iteration + chi(\"seed\")) * num );\n        \n        int new_cur = pts[index];\n        vector dir = rand(@ptnum + ch(\"seed\"));\n        setpointattrib(0, \"dir\", new_cur, dir, \"set\");\n        setpointgroup(0, \"current\", new_cur, 1, \"set\");\n        setpointgroup(0, \"novisit\", new_cur, 0, \"set\");\n    }\n    \n}else{\n    i@stop = 1;\n}")


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code to establish connections for /obj/geo1/bound1
hou_node = hou_parent.node("bound1")
if hou_parent.node("box1") is not None:
    hou_node.setInput(0, hou_parent.node("box1"), 0)
# Code to establish connections for /obj/geo1/convertline1
hou_node = hou_parent.node("convertline1")
if hou_parent.node("bound1") is not None:
    hou_node.setInput(0, hou_parent.node("bound1"), 0)
# Code to establish connections for /obj/geo1/initial_dir
hou_node = hou_parent.node("initial_dir")
if hou_parent.node("group3") is not None:
    hou_node.setInput(0, hou_parent.node("group3"), 0)
# Code to establish connections for /obj/geo1/group1
hou_node = hou_parent.node("group1")
if hou_parent.node("convertline1") is not None:
    hou_node.setInput(0, hou_parent.node("convertline1"), 0)
# Code to establish connections for /obj/geo1/group2
hou_node = hou_parent.node("group2")
if hou_parent.node("group1") is not None:
    hou_node.setInput(0, hou_parent.node("group1"), 0)
# Code to establish connections for /obj/geo1/group3
hou_node = hou_parent.node("group3")
if hou_parent.node("group2") is not None:
    hou_node.setInput(0, hou_parent.node("group2"), 0)
# Code to establish connections for /obj/geo1/foreach_end1
hou_node = hou_parent.node("foreach_end1")
if hou_parent.node("add_cur_if_lost") is not None:
    hou_node.setInput(0, hou_parent.node("add_cur_if_lost"), 0)
# Code to establish connections for /obj/geo1/foreach_begin1
hou_node = hou_parent.node("foreach_begin1")
if hou_parent.node("compile_begin1") is not None:
    hou_node.setInput(0, hou_parent.node("compile_begin1"), 0)
# Code to establish connections for /obj/geo1/compile_end1
hou_node = hou_parent.node("compile_end1")
if hou_parent.node("foreach_end1") is not None:
    hou_node.setInput(0, hou_parent.node("foreach_end1"), 0)
# Code to establish connections for /obj/geo1/compile_begin1
hou_node = hou_parent.node("compile_begin1")
if hou_parent.node("initial_cur_num") is not None:
    hou_node.setInput(0, hou_parent.node("initial_cur_num"), 0)
# Code to establish connections for /obj/geo1/path_iteration
hou_node = hou_parent.node("path_iteration")
if hou_parent.node("attribcreate1") is not None:
    hou_node.setInput(0, hou_parent.node("attribcreate1"), 0)
# Code to establish connections for /obj/geo1/polywire1
hou_node = hou_parent.node("polywire1")
if hou_parent.node("compile_end1") is not None:
    hou_node.setInput(0, hou_parent.node("compile_end1"), 0)
# Code to establish connections for /obj/geo1/initial_cur_num
hou_node = hou_parent.node("initial_cur_num")
if hou_parent.node("initial_dir") is not None:
    hou_node.setInput(0, hou_parent.node("initial_dir"), 0)
# Code to establish connections for /obj/geo1/attribcreate1
hou_node = hou_parent.node("attribcreate1")
if hou_parent.node("foreach_begin1") is not None:
    hou_node.setInput(0, hou_parent.node("foreach_begin1"), 0)
# Code to establish connections for /obj/geo1/add_cur_if_lost
hou_node = hou_parent.node("add_cur_if_lost")
if hou_parent.node("path_iteration") is not None:
    hou_node.setInput(0, hou_parent.node("path_iteration"), 0)
if hou_parent.node("foreach_count1") is not None:
    hou_node.setInput(3, hou_parent.node("foreach_count1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

