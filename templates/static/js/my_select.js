var hello = function () {
    console.log('hell django');
};

var SelectInt = function (defaultProjectId, defaultModuleId) {
    console.log(defaultProjectId, defaultModuleId);
    var cmbProject = $("selectProject");
    var cmbModule = $("selectModule");

    console.log(cmbProject, cmbModule);

    var dataList = [];
    
    //设置默认选项
    function setDefaultOption(obj,id) {
        for (let i =0;i<obj.options.length;i++){

        }
    }
};