#ifndef EXAMPLE_H
#define EXAMPLE_H

#include <godot_cpp/classes/node.hpp>

using namespace godot;

class Example : public Node {
    GDCLASS(Example, Node)

public:
    Example();
    ~Example();

private:

protected:
    static void _bind_methods();
};

#endif