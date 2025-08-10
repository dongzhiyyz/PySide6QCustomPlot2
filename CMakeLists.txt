cmake_minimum_required(VERSION 3.18)
project(PySide6QCustomPlot2)

# Main tuning variables:
set(MY_SITE_PACKAGES_PATH "${CMAKE_CURRENT_SOURCE_DIR}/.venv/Lib/site-packages")
set(MY_PYTHON_INSTALL_PATH "C:/Users/dongz/AppData/Local/Programs/Python/Python311")
set(MY_QT_INSTALL D:/Qt/6.7.3/msvc2019_64)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_PREFIX_PATH ${MY_QT_INSTALL})
set(CMAKE_BUILD_TYPE Release)

message("\n")
message(STATUS "********************************************************************************************")
message(STATUS "Python3_ROOT_DIR: ${Python3_ROOT_DIR}")
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_FIND_REGISTRY: ${Python3_FIND_REGISTRY}")
message(STATUS "PY_BUILD_CMAKE_MODULE_NAME: ${PY_BUILD_CMAKE_MODULE_NAME}")
message(STATUS "********************************************************************************************")
message("\n")


find_package(Qt6 REQUIRED COMPONENTS Core Widgets PrintSupport)

qt_standard_project_setup()


set(SHIBOKEN_OUTPUT_FOLDER "${CMAKE_CURRENT_BINARY_DIR}/OUTPUTDIR")

# Do not use a GLOB here, to allow for usage as OUTPUT in custom command
set(SHIBOKEN_GENERATED_SOURCES
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/pyside6qcustomplot2_module_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/pyside6qcustomplot2_python.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcp_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcp_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractplottable_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractplottable_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxis_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxis_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxisrect_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxisrect_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxisticker_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxisticker_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpdataselection_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpdataselection_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraph_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraph_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraphdata_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraphdata_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgrid_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgrid_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayer_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayer_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayerable_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayerable_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayout_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayout_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutelement_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutelement_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutgrid_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutgrid_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplegend_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplegend_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplineending_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplineending_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcppainter_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcppainter_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpplottableinterface1d_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpplottableinterface1d_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcprange_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcprange_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpscatterstyle_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpscatterstyle_wrapper.h"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcustomplot_wrapper.cpp"
    "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcustomplot_wrapper.h"

     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpselectiondecorator_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpselectiondecorator_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxistickerlog_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxistickerlog_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpdatarange_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpdatarange_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraphdatacontainer_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpgraphdatacontainer_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurvedatacontainer_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurvedatacontainer_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpvector2d_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpvector2d_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractitem_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractitem_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemtracer_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemtracer_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemposition_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemposition_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemanchor_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemanchor_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxispainterprivate_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxispainterprivate_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpselectionrect_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpselectionrect_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurve_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurve_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurvedata_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpcurvedata_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemtext_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemtext_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemstraightline_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpitemstraightline_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxistickerdatetime_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpaxistickerdatetime_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractlegenditem_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpabstractlegenditem_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpplottablelegenditem_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcpplottablelegenditem_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpaxisticker_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpaxisticker_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpgraphdatacontainer_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpgraphdatacontainer_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpcurvedatacontainer_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qsharedpointer_qcpcurvedatacontainer_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/keyvalues_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/keyvalues_wrapper.h"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutinset_wrapper.cpp"
     "${SHIBOKEN_OUTPUT_FOLDER}/PySide6QCustomPlot2/qcplayoutinset_wrapper.h"
)

add_custom_command(
    COMMAND shiboken6
        --generator-set=shiboken
        --output-directory=OUTPUTDIR
        -I${MY_QT_INSTALL}/include -I${MY_QT_INSTALL}/include/QtCore
        --typesystem-paths=${MY_SITE_PACKAGES_PATH}/PySide6/typesystems
        --enable-pyside-extensions
        --avoid-protected-hack
        ${CMAKE_CURRENT_SOURCE_DIR}/src/wrapper.hpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/bindings.xml
    DEPENDS src/bindings.xml src/wrapper.hpp
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    OUTPUT ${SHIBOKEN_GENERATED_SOURCES}
    COMMENT "Running shiboken6 generator for src/bindings.xml"
)

add_custom_target(run_shiboken
    DEPENDS ${SHIBOKEN_GENERATED_SOURCES}
)

add_library(
    PySide6QCustomPlot2
    SHARED
    src/wrapper.hpp
    src/qcustomplot.cpp
    src/qcustomplot.h
    ${SHIBOKEN_GENERATED_SOURCES}
)

# A bit ugly:
# - include paths to python installation
# - include paths to pyside and shiboken6_generator in .venv
target_include_directories(
    PySide6QCustomPlot2
    PRIVATE
    "src"
    "${MY_PYTHON_INSTALL_PATH}/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtWidgets"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtGui"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtCore"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtPrintSupport"
    "${MY_SITE_PACKAGES_PATH}/shiboken6_generator/include"
)

# Use the python stable ABI3:
# See also https://docs.python.org/3/c-api/stable.html
target_compile_definitions(
    PySide6QCustomPlot2
    PRIVATE
    "-DPy_LIMITED_API=0x03080000"
)

set_target_properties(
    PySide6QCustomPlot2
    PROPERTIES
    SUFFIX ".pyd"
)

target_link_directories(
    PySide6QCustomPlot2
    PRIVATE
    "${MY_PYTHON_INSTALL_PATH}/libs"
    ${MY_SITE_PACKAGES_PATH}/shiboken6
    ${MY_SITE_PACKAGES_PATH}/PySide6
)

target_link_libraries(
    PySide6QCustomPlot2
    PRIVATE
    Qt6::Widgets
    Qt6::Core
    Qt6::PrintSupport
    shiboken6.abi3
    pyside6.abi3
)

install(
    TARGETS PySide6QCustomPlot2
    DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
)
