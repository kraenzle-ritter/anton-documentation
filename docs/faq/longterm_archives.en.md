# Anton as a digital long-term archive

Digital preservation is a highly complex and multi-layered task, for which Anton can be deployed either [as a service](anton_as_service.md) or [on premises](anton_on_premises.md).

So-called _bitstream preservation_ – the actual storage and safeguarding of the data – is provided by the operating infrastructure, not by the application. **With Anton as a Service**, that is, when running on our servers, the digital data is stored on a suitable infrastructure that keeps three copies at three locations – sixfold redundancy in total.

!!! note "On premises"
    Anyone running Anton on their own servers is responsible for storage, redundancy and backup themselves. The infrastructure described here is part of our operations and is not supplied with the software. We are happy to advise on setting it up.

Anton keeps a checksum for every file, so that the integrity of the data can be verified – that is, it can be determined whether data has been altered or damaged. This check is not an automatic function of the application; it is set up per installation as a recurring job. On our servers it is set up for the large archives. In installations with a connected long-term archive (DIMAG), that system is responsible for bitstream preservation. More on this under [Digital preservation: overview](../admin/preservation.md).

Access to the data is exclusively through Anton, which permits authorised access only. In the case of legally protected data, additional criteria such as the permissible server location may need to be clarified. Thanks to the metadata in Anton, the data is easy to locate and available quickly at all times.

We are happy to support our customers in preparing the _transfer_ (appraisal, ingest, pre-ingest, etc.) and with _preservation planning_.

## Preservation planning

### Format identification

Format identification based on the MIME type or the file extension is complemented in Anton by the integration of [Siegfried](https://www.itforarchivists.com/siegfried) and/or [Fido](https://github.com/openpreserve/fido). Both tools identify file formats by means of [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. This allows file formats to be determined precisely for digital preservation.

### Risk assessment

Using the PRONOM IDs, we can attempt to apply the risk assessment of the [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation) in Anton. This assessment can help in deciding which preservation measures are necessary.

In Anton's admin area, an overview of the file formats present in the archive together with their risk assessment can be displayed.
