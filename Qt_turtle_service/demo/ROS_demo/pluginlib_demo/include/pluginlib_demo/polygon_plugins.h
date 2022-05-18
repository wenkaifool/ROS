#ifndef PLUGINLIB_DEMO__POLYGON_PLUGINS_H_
#define PLUGINLIB_DEMO__POLYGON_PLUGINS_H_

#include <pluginlib_demo/polygon_base.h>
#include <cmath>

namespace polygon_plugins
{
  class Triangle : public polygon_base::RegularPolygon
  {
    public:
      Triangle(){}

      void initialize(double side_length)
      {
        side_length_ = side_length;
      }

      double area()
      {
        return 0.5 * side_length_ * getHeight();
      }

      double getHeight()
      {
        return sqrt((side_length_ * side_length_) - ((side_length_ / 2) * (side_length_ / 2)));
      }
      double getlength()
      {
          return side_length_ * 3.0;
      }

    private:
      double side_length_;
  };

  class Square : public polygon_base::RegularPolygon
  {
    public:
      Square(){}

      void initialize(double side_length)
      {
        side_length_ = side_length;
      }

      double area()
      {
        return side_length_ * side_length_;
      }

      double getlength()
      {
          return side_length_ * 4.0;
      }

    private:
      double side_length_;

  };
};
#endif
