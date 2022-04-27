
set(CPACK_PACKAGE_NAME "mkr-file-format")
set(CPACK_PACKAGE_VENDOR "Oxford Nanopore")
set(CPACK_VERBATIM_VARIABLES true)
set(CPACK_PACKAGE_VERSION_MAJOR ${MKR_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${MKR_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${MKR_VERSION_REV})
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE.md")

include(CPack)