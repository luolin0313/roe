# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ansible_CallBack_Model_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name=b'\xe8\xbe\x93\xe5\x87\xba\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='Ansible_CallBack_PlayBook_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name=b'\xe8\xbe\x93\xe5\x87\xba\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='Ansible_Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.CharField(max_length=200, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('user', models.SmallIntegerField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\xba')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'opsmanage_ansible_inventory',
                'verbose_name': 'Ansible\u8d44\u4ea7\u8868',
                'verbose_name_plural': 'Ansible\u8d44\u4ea7\u8868',
                'permissions': (('can_read_ansible_inventory', '\u8bfb\u53d6ansible\u8d44\u4ea7\u6743\u9650'), ('can_change_ansible_inventory', '\u66f4\u6539ansbile\u8d44\u4ea7\u6743\u9650'), ('can_add_ansible_inventory', '\u6dfb\u52a0ansible\u8d44\u4ea7\u6743\u9650'), ('can_delete_ansible_inventory', '\u5220\u9664ansible\u8d44\u4ea7\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Ansible_Inventory_Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, verbose_name=b'group name')),
                ('ext_vars', models.TextField(blank=True, null=True, verbose_name=b'\xe7\xbb\x84\xe5\xa4\x96\xe9\x83\xa8\xe5\x8f\x98\xe9\x87\x8f')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_group', to='OpsControl.Ansible_Inventory')),
            ],
            options={
                'db_table': 'opsmanage_ansible_inventory_groups',
                'verbose_name': 'Ansible\u8d44\u4ea7\u6210\u5458\u8868',
                'verbose_name_plural': 'Ansible\u8d44\u4ea7\u6210\u5458\u8868',
            },
        ),
        migrations.CreateModel(
            name='Ansible_Inventory_Groups_Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.SmallIntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_group_server', to='OpsControl.Ansible_Inventory_Groups')),
            ],
            options={
                'db_table': 'opsmanage_ansible_inventory_groups_servers',
            },
        ),
        migrations.CreateModel(
            name='Ansible_Playbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_name', models.CharField(max_length=50, unique=True, verbose_name=b'\xe5\x89\xa7\xe6\x9c\xac\xe5\x90\x8d\xe7\xa7\xb0')),
                ('playbook_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('playbook_vars', models.TextField(blank=True, null=True, verbose_name=b'\xe6\xa8\xa1\xe5\x9d\x97\xe5\x8f\x82\xe6\x95\xb0')),
                ('playbook_uuid', models.CharField(max_length=50, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80id')),
                ('playbook_server_model', models.CharField(blank=True, choices=[(b'service', 'service'), (b'group', 'group'), (b'custom', 'custom')], max_length=10, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe9\x80\x89\xe6\x8b\xa9\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('playbook_server_value', models.SmallIntegerField(blank=True, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe9\x80\x89\xe6\x8b\xa9\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x80\xbc')),
                ('playbook_file', models.FileField(upload_to=b'./playbook/', verbose_name=b'\xe5\x89\xa7\xe6\x9c\xac\xe8\xb7\xaf\xe5\xbe\x84')),
                ('playbook_auth_group', models.SmallIntegerField(blank=True, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xbb\x84')),
                ('playbook_auth_user', models.SmallIntegerField(blank=True, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\x94\xa8\xe6\x88\xb7')),
                ('playbook_type', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name=b'\xe5\x89\xa7\xe6\x9c\xac\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'db_table': 'opsmanage_ansible_playbook',
                'verbose_name': 'Ansible\u5267\u672c\u914d\u7f6e\u8868',
                'verbose_name_plural': 'Ansible\u5267\u672c\u914d\u7f6e\u8868',
                'permissions': (('can_read_ansible_playbook', '\u8bfb\u53d6Ansible\u5267\u672c\u6743\u9650'), ('can_change_ansible_playbook', '\u66f4\u6539Ansible\u5267\u672c\u6743\u9650'), ('can_add_ansible_playbook', '\u6dfb\u52a0Ansible\u5267\u672c\u6743\u9650'), ('can_delete_ansible_playbook', '\u5220\u9664Ansible\u5267\u672c\u6743\u9650'), ('can_exec_ansible_playbook', '\u6267\u884cAnsible\u5267\u672c\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Ansible_Playbook_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_server', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_number', to='OpsControl.Ansible_Playbook')),
            ],
            options={
                'db_table': 'opsmanage_ansible_playbook_number',
                'verbose_name': 'Ansible\u5267\u672c\u6210\u5458\u8868',
                'verbose_name_plural': 'Ansible\u5267\u672c\u6210\u5458\u8868',
                'permissions': (('can_read_ansible_playbook_number', '\u8bfb\u53d6Ansible\u5267\u672c\u6210\u5458\u6743\u9650'), ('can_change_ansible_playbook_number', '\u66f4\u6539Ansible\u5267\u672c\u6210\u5458\u6743\u9650'), ('can_add_ansible_playbook_number', '\u6dfb\u52a0Ansible\u5267\u672c\u6210\u5458\u6743\u9650'), ('can_delete_ansible_playbook_number', '\u5220\u9664Ansible\u5267\u672c\u6210\u5458\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Ansible_Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_name', models.CharField(max_length=50, unique=True, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe5\x90\x8d\xe7\xa7\xb0')),
                ('script_uuid', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80id')),
                ('script_server', models.TextField(blank=True, max_length=200, null=True, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe6\x9c\xba\xe5\x99\xa8')),
                ('script_file', models.FileField(upload_to=b'./script/', verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe8\xb7\xaf\xe5\xbe\x84')),
                ('script_args', models.TextField(blank=True, null=True, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe5\x8f\x82\xe6\x95\xb0')),
                ('script_service', models.SmallIntegerField(blank=True, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe4\xb8\x9a\xe5\x8a\xa1')),
                ('script_group', models.SmallIntegerField(blank=True, null=True, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe7\xbb\x84')),
                ('script_type', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'db_table': 'opsmanage_ansible_script',
                'verbose_name': 'Ansible\u811a\u672c\u914d\u7f6e\u8868',
                'verbose_name_plural': 'Ansible\u811a\u672c\u914d\u7f6e\u8868',
                'permissions': (('can_read_ansible_script', '\u8bfb\u53d6Ansible\u811a\u672c\u6743\u9650'), ('can_change_ansible_script', '\u66f4\u6539Ansible\u811a\u672c\u6743\u9650'), ('can_add_ansible_script', '\u6dfb\u52a0Ansible\u811a\u672c\u6743\u9650'), ('can_delete_ansible_script', '\u5220\u9664Ansible\u811a\u672c\u6743\u9650'), ('can_exec_ansible_script', '\u6267\u884cAnsible\u811a\u672c\u6743\u9650'), ('can_exec_ansible_model', '\u6267\u884cAnsible\u6a21\u5757\u6743\u9650'), ('can_read_ansible_model', '\u8bfb\u53d6Ansible\u6a21\u5757\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Log_Ansible_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_user', models.CharField(default=None, max_length=50, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe7\x94\xa8\xe6\x88\xb7')),
                ('ans_model', models.CharField(default=None, max_length=100, verbose_name=b'\xe6\xa8\xa1\xe5\x9d\x97\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ans_args', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name=b'\xe6\xa8\xa1\xe5\x9d\x97\xe5\x8f\x82\xe6\x95\xb0')),
                ('ans_server', models.TextField(default=None, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'opsmanage_log_ansible_model',
                'verbose_name': 'Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u8868',
                'verbose_name_plural': 'Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u8868',
                'permissions': (('can_read_log_ansible_model', '\u8bfb\u53d6Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_change_log_ansible_model', '\u66f4\u6539Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_add_log_ansible_model', '\u6dfb\u52a0Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_delete_log_ansible_model', '\u5220\u9664Ansible\u6a21\u5757\u6267\u884c\u8bb0\u5f55\u6743\u9650')),
            },
        ),
        migrations.CreateModel(
            name='Log_Ansible_Playbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_id', models.IntegerField(blank=True, default=None, null=True, verbose_name=b'id')),
                ('ans_user', models.CharField(default=None, max_length=50, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe7\x94\xa8\xe6\x88\xb7')),
                ('ans_name', models.CharField(default=None, max_length=100, verbose_name=b'\xe6\xa8\xa1\xe5\x9d\x97\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ans_content', models.CharField(default=None, max_length=100)),
                ('ans_server', models.TextField(default=None, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'opsmanage_log_ansible_playbook',
                'verbose_name': 'Ansible\u5267\u672c\u64cd\u4f5c\u8bb0\u5f55\u8868',
                'verbose_name_plural': 'Ansible\u5267\u672c\u64cd\u4f5c\u8bb0\u5f55\u8868',
                'permissions': (('can_read_log_ansible_playbook', '\u8bfb\u53d6Ansible\u5267\u672c\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_change_log_ansible_playbook', '\u66f4\u6539Ansible\u5267\u672c\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_add_log_ansible_playbook', '\u6dfb\u52a0Ansible\u5267\u672c\u6267\u884c\u8bb0\u5f55\u6743\u9650'), ('can_delete_log_ansible_playbook', '\u5220\u9664Ansible\u5267\u672c\u6267\u884c\u8bb0\u5f55\u6743\u9650')),
            },
        ),
        migrations.AddField(
            model_name='ansible_callback_playbook_result',
            name='logId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpsControl.Log_Ansible_Playbook'),
        ),
        migrations.AddField(
            model_name='ansible_callback_model_result',
            name='logId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpsControl.Log_Ansible_Model'),
        ),
        migrations.AlterUniqueTogether(
            name='ansible_inventory_groups_server',
            unique_together=set([('groups', 'server')]),
        ),
        migrations.AlterUniqueTogether(
            name='ansible_inventory_groups',
            unique_together=set([('inventory', 'group_name')]),
        ),
    ]
