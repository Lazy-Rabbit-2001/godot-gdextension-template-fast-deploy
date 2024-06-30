#include "register_types.h"

#include <gdextension_interface.h>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/godot.hpp>

#include "example.h"
#include "doc_data_example.gen.h"

void initialize_gdextension_types(ModuleInitializationLevel p_level)
{
	if (p_level == MODULE_INITIALIZATION_LEVEL_SCENE) {
		// Registers the class(es)
		ClassDB::register_class<Example>();
	}

	if (p_level == MODULE_INITIALIZATION_LEVEL_EDITOR) {
		// Registers the documentation for the class(es)
		GDExtensionsInterfaceEditorHelpLoadXmlFromUtf8CharsAndLen editor_help_load_xml_from_utf8_chars_and_len = (GDExtensionsInterfaceEditorHelpLoadXmlFromUtf8CharsAndLen)internal::gdextension_interface_get_proc_address("editor_help_load_xml_from_utf8_chars_and_len");
		editor_help_load_xml_from_utf8_chars_and_len(_doc_data, _doc_data_size);
	}
	
}

void uninitialize_gdextension_types(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}
}

extern "C"
{
	// Initialization
	GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)
	{
		GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);
		init_obj.register_initializer(initialize_gdextension_types);
		init_obj.register_terminator(uninitialize_gdextension_types);
		init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

		return init_obj.init();
	}
}