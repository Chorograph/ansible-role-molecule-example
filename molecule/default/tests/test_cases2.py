def test_testfolder(host):
    f = host.file('/tmp/testfolder')

    assert f.exists
    assert f.user == 'James'
    assert f.group == 'admin'
