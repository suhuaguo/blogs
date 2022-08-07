if __name__ == "__main__":    printCopyright()    parser = getOptionParser()    options, args = parser.parse_args(sys.argv[1:])    if options.reader is not None and options.writer is not None:        generateJobConfigTemplate(options.reader,options.writer)        sys.exit(RET_STATE['OK'])    if len(args) != 1:        parser.print_help()        sys.exit(RET_STATE['FAIL'])    # 获取启动命令的各种参数，注意命令参数的顺序，其中第 0 个参数为 job 配置路径    startCommand = buildStartCommand(options, args)    # print startCommand    # 开启子进程，拉起 DataX 任务;对应 Java 类是：com.alibaba.datax.core.Engine     child_process = subprocess.Popen(startCommand, shell=True)    register_signal()    (stdout, stderr) = child_process.communicate()    sys.exit(child_process.returncode)
