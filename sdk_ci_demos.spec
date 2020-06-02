/*
A KBase module: sdk_ci_demos
This sample module contains one small method that filters contigs.
*/

module sdk_ci_demos {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_sdk_ci_demos(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
