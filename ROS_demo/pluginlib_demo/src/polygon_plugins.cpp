#include "pluginlib_demo/polygon_plugins.h"
#include "pluginlib_demo/polygon_base.h"
#include "pluginlib/class_list_macros.h"

PLUGINLIB_EXPORT_CLASS (polygon_plugins::Triangle, polygon_base::RegularPolygon);
PLUGINLIB_EXPORT_CLASS (polygon_plugins::Square, polygon_base::RegularPolygon);