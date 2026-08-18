# Anton as a Service

Anton runs on a server rented by k & r from a leading provider (located in Switzerland). k & r is responsible both for setting up and maintaining the server (hardening, monitoring, operating-system updates and upgrades) and for setting up and maintaining Anton (updates and upgrades).

A backup of the production server is stored daily on two servers at two different locations in Switzerland. Both run as RAID 1. Together with the production data and the encrypted local backup on the production server, the data therefore exists sixfold, distributed across three locations (see [Infrastructure](infrastructure.md)). A further server continuously monitors the machines involved, so that k & r is informed of any problem at all times and can intervene quickly.

## Advantages

- archive staff only need internet access and a current web browser  
- constant, predictable costs  
- optimal alignment of infrastructure (server operating system, installed software) and the Anton installation  

## Disadvantages

- possibly more expensive than a dedicated server solution for very large data volumes  
- with sensitive data: the data is not held on the institution's own server  
- with highly sensitive data: the data is managed over the internet (not recommended)  

## Costs

Anton is intended to enable small and medium-sized archives in particular to catalogue their holdings professionally and sustainably. The costly infrastructure is therefore shared between several Anton customers. This allows updates and upgrades to be applied quickly and inexpensively at any time. A separate data directory (PDFs, images, logo, etc.) and a separate database are created for each instance (customer). This structure keeps the effort for setting up and maintaining Anton comparatively low. At the same time, customer data remains well encapsulated and can easily be handled as a whole.
